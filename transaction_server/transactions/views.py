from http.client import HTTPResponse
from pydoc import ModuleScanner
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from socket import gethostname
from json import loads

from .models import *

from datetime import datetime, timezone

# Create your views here.
@csrf_exempt
def index(request):
	return HttpResponse("This is the transaction server.")

@csrf_exempt
def workload(request):
	if request.method != 'POST':
		return HttpResponseNotAllowed(['POST'])

	workload_data = {}
	try:
		workload_data = loads(request.body)
	except:
		return HttpResponseBadRequest("Request must be a JSON array.")

	workload_transactions = []
	for user_command in workload_data:
		transaction = Transaction(
				server = gethostname(),
				command = user_command['command'],
		)
		workload_transactions.append(transaction)
	Transaction.objects.bulk_create(workload_transactions)
	return HttpResponse("Successfully ran workload.")

class QuoteServer:
	def __init__(self):
		pass
	def get_quote(self, userid, stock_symbol):
		return 100

class UserManager:
	def __init__(self, userid):
		self.user = User.objects.get(userid=userid)
	def add_funds(self, amount):
		self.user.funds += amount
		self.user.save()
	def get_funds(self):
		return self.user.funds
	def uncommit_buy(self, stock_symbol, amount):
		# quote_server = QuoteServer()
		# quote = quote_server.get_quote(self.user.userid, stock_symbol)
		try:
			buy = UncommittedBuy.objects.get(user=self.user)
			buy.delete()
		except UncommittedBuy.DoesNotExist:
			pass
		buy = UncommittedBuy(user=self.user, stock_symbol=stock_symbol, funds=amount, timestamp=datetime.now())
		buy.save()
	def has_recent_buy(self):
		try:
			buy = UncommittedBuy.objects.get(user=self.user)
			buy_timestamp = buy.timestamp
			current_time = datetime.now(timezone.utc)
			time_difference = current_time - buy_timestamp
			return time_difference.total_seconds() < 60
		except UncommittedBuy.DoesNotExist:
			return False
	def commit_buy(self):
		buy = UncommittedBuy.objects.get(user=self.user)
		try:
			stock_account = StockAccount.objects.get(user=self.user,stock_symbol=buy.stock_symbol)
		except StockAccount.DoesNotExist:
			stock_account = StockAccount(user=self.user,stock_symbol=buy.stock_symbol,amount=0)
		self.user.funds -= buy.funds
		self.user.save()
		quote_server = QuoteServer()
		quote = quote_server.get_quote(self.user.userid, buy.stock_symbol)
		stock_account.amount += (buy.funds * 100)/quote

		buy.delete()
		stock_account.save()
	def cancel_buy(self):
		try:
			buy = UncommittedBuy.objects.get(user=self.user)
			buy.delete()
		except UncommittedBuy.DoesNotExist:
			pass

		
		



def create_user(request, userid):
	user = User(userid=userid, funds=0)
	user.save()
	return HttpResponse("user created.")

def add(request, userid, amount):
	user = UserManager(userid)
	user.add_funds(amount)
	return HttpResponse("Added funds.")

def buy(request, userid, stock_symbol, amount):
	user = UserManager(userid)

	if user.get_funds() < amount:
		# display error
		return HttpResponse("Not enough funds.")
	else:
		user.uncommit_buy(stock_symbol, amount)
		return HttpResponse("created uncommitted buy.")


def commit_buy(request, userid):
	user = UserManager(userid)
	if not user.has_recent_buy():
		# display error
		return HttpResponse("no uncommitted buy.")
	else:
		user.commit_buy()
		return HttpResponse("committed buy.")
def cancel_buy(request, userid):
	user = UserManager(userid)
	user.cancel_buy()
	return HttpResponse("cancelled uncommitted, if any.")

