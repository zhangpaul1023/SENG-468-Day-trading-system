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
	
	def uncommit_sell(self, stock_symbol, amount):
		try:
			sell = UncommittedSell.objects.get(user=self.user)
			sell.delete()
		except UncommittedSell.DoesNotExist:
			pass
		sell = UncommittedSell(user=self.user, stock_symbol=stock_symbol, funds=amount, timestamp=datetime.now())
		sell.save()

	def has_recent_buy(self):
		try:
			buy = UncommittedBuy.objects.get(user=self.user)
			buy_timestamp = buy.timestamp
			current_time = datetime.now(timezone.utc)
			time_difference = current_time - buy_timestamp
			return time_difference.total_seconds() < 60
		except UncommittedBuy.DoesNotExist:
			return False

	def has_recent_sell(self):
		try:
			sell = UncommittedSell.objects.get(user=self.user)
			sell_timestamp = sell.timestamp
			current_time = datetime.now(timezone.utc)
			time_difference = current_time - sell_timestamp
			return time_difference.total_seconds() < 60
		except UncommittedSell.DoesNotExist:
			return False

	def create_buy_amount(self, stock_symbol, amount):
		buy = BuyTrigger(user=self.user,stock_symbol=stock_symbol,amount=amount,triggerAmount=0)
		buy.save()

	def set_buy_trigger(self, stock_symbol, amount):
		buy = BuyTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
		buy.triggerAmount = amount
		buy.save()

	def cancel_set_buy(self, stock_symbol):
		buy = BuyTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
		buy.delete()

	def create_sell_amount(self, stock_symbol, amount):
		sell = SellTrigger(user=self.user,stock_symbol=stock_symbol,amount=amount,triggerAmount=999999)
		sell.save()

	def set_sell_trigger(self, stock_symbol, amount):
		sell = SellTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
		sell.triggerAmount = amount
		sell.save()

	def cancel_set_buy(self, stock_symbol):
		sell = SellTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
		sell.delete()




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

	def commit_sell(self):
		sell = UncommittedSell.objects.get(user=self.user)
		try:
			stock_account = StockAccount.objects.get(user=self.user,stock_symbol=sell.stock_symbol)
		except StockAccount.DoesNotExist:
			stock_account = StockAccount(user=self.user,stock_symbol=sell.stock_symbol,amount=0)
		self.user.funds += sell.funds
		self.user.save()
		quote_server = QuoteServer()
		quote = quote_server.get_quote(self.user.userid, sell.stock_symbol)
		stock_account.amount -= (sell.funds * 100)/quote

		sell.delete()
		stock_account.save()

	def cancel_buy(self):
		try:
			buy = UncommittedBuy.objects.get(user=self.user)
			buy.delete()
		except UncommittedBuy.DoesNotExist:
			pass

	def cancel_sell(self):
		try:
			sell = UncommittedSell.objects.get(user=self.user)
			sell.delete()
		except UncommittedSell.DoesNotExist:
			pass

	def stock(self, stock_symbol):
		try:
			stock_account = StockAccount.objects.get(user=self.user,stock_symbol=stock_symbol)
		except StockAccount.DoesNotExist:
			stock_account = StockAccount(user=self.user,stock_symbol=stock_symbol,amount=0)
		quote_server = QuoteServer()
		quote = quote_server.get_quote(self.user.userid, sell.stock_symbol)
		return stock_symbol.amount * quote

	def has_set_buy(self, stock_symbol):
		try:
			buy = BuyTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
			return True
		except BuyTrigger.DoesNotExist:
			return False

	def has_set_sell(self, stock_symbol):
		try:
			sell = SellTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
			return True
		except SellTrigger.DoesNotExist:
			return False



		
		



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

def sell(request, userid, stock_symbol, amount):
	user = UserManager(userid)
	
	if user.stock(stock_symbol) < amount:
		# display error
		return HttpResponse("Not enough Stock.")
	else:
		user.uncommit_sell(stock_symbol, amount)
		return HttpResponse("created uncommitted sell.")

def commit_buy(request, userid):
	user = UserManager(userid)
	if not user.has_recent_buy():
		# display error
		return HttpResponse("no uncommitted buy.")
	else:
		user.commit_buy()
		return HttpResponse("committed buy.")

def commit_sell(request, userid):
	user = UserManager(userid)
	if not user.has_recent_sell():
		# display error
		return HttpResponse("no uncommitted sell.")
	else:
		user.cancel_sell()
		return HttpResponse("committed sell.")

def cancel_buy(request, userid):
	user = UserManager(userid)
	user.cancel_buy()
	return HttpResponse("cancelled uncommitted, if any.")

def cancel_sell(request, userid):
	user = UserManager(userid)
	user.cancel_sell()
	return HttpResponse("cancelled uncommitted, if any.")

def set_buy_amount(userid, stock_symbol, amount):
	user = UserManager(userid)
	if user.get_funds() < amount:
		# display error
		return HttpResponse('not enough funds')
	else:
		user.create_buy_amount(stock_symbol, amount)
		return HttpResponse('created set buy')

def set_buy_trigger(request, userid, stock_symbol, amount):
	user = UserManager(userid)
	if not user.has_set_buy(stock_symbol):
		# display error
		return HttpResponse('no set buy')
	else:
		user.set_buy_trigger(stock_symbol, amount)
		return HttpResponse('created buy trigger')

def cancel_set_buy(request, userid, stock_symbol):
	user = UserManager(userid)
	if not user.has_set_buy(stock_symbol):
		# display error
		return HttpResponse('no set buy')
	else:
		user.cancel_set_buy(stock_symbol)
		return HttpResponse('cancelled set buy')

def set_sell_amount(request, userid, stock_symbol, amount):
	user = UserManager(userid)
	if user.stock(stock_symbol) < amount:
		# display error
		return HttpResponse('not enough stock')
	else:
		user.create_sell_amount(stock_symbol, amount)
		return HttpResponse('cancelled set sell')

def set_sell_trigger(request, userid, stock_symbol, amount):
	user = UserManager(userid)
	if not user.has_set_sell(stock_symbol):
		# display error
		return HttpResponse('no set sell')
	else:
		user.set_sell_trigger(stock_symbol, amount)
		return HttpResponse('created sell trigger')

def cancel_set_sell(request, userid, stock_symbol):
	user = UserManager(userid)
	if not user.has_set_sell(stock_symbol):
		# display error
		return HttpResponse('no set sell')
	else:
		user.cancel_set_sell(stock_symbol)
		return HttpResponse('cancelled sell trigger')

