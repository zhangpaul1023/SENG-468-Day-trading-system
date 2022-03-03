from ast import Add
from distutils.log import error
from http.client import HTTPResponse
from pydoc import ModuleScanner
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from transactions.models import UserAccount

from transactions.models import Transaction
from transactions.models import AddCommand
from transactions.models import QuoteCommand
from transactions.models import BuyCommand
from transactions.models import SellCommand
from transactions.models import CommitBuyCommand
from transactions.models import CommitSellCommand
from transactions.models import CancelBuyCommand
from transactions.models import CancelSellCommand
from transactions.models import SetBuyAmountCommand
from transactions.models import SetSellAmountCommand
from transactions.models import CancelSetBuyCommand
from transactions.models import CancelSetSellCommand
from transactions.models import SetBuyTriggerCommand
from transactions.models import SetSellTriggerCommand
from transactions.models import DumplogCommand
from transactions.models import DisplaySummaryCommand

from socket import gethostname
from json import loads

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

	server = gethostname()
	for user_command in workload_data:
		if user_command['command'] == Transaction.Command.DUMPLOG and not 'userId' in user_command:
			continue

		user_account = UserAccount.objects.filter(account_name=user_command['userId']).first()
		if user_account == None:
			return HttpResponseForbidden("Unable to access resources of user.")

		if user_command['command'] == Transaction.Command.ADD:
			transaction = AddCommand(
				server = server,
				amount = user_command['amount'],
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.QUOTE:
			transaction = QuoteCommand(
				server = server,
				stock_symbol = user_command['symbol'],
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.BUY:
			transaction = BuyCommand(
				server = server,
				stock_symbol = user_command['symbol'],
				amount = user_command['amount'],
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.COMMIT_BUY:
			transaction = CommitBuyCommand(
				server = server,
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.CANCEL_BUY:
			transaction = CancelBuyCommand(
				server = server,
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.SELL:
			transaction = SellCommand(
				server = server,
				stock_symbol = user_command['symbol'],
				amount = user_command['amount'],
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.COMMIT_SELL:
			transaction = CommitSellCommand(
				server = server,
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.CANCEL_SELL:
			transaction = CancelSellCommand(
				server = server,
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.SET_BUY_AMOUNT:
			transaction = SetBuyAmountCommand(
				server = server,
				stock_symbol = user_command['symbol'],
				amount = user_command['amount'],
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.CANCEL_SET_BUY:
			transaction = CancelSetBuyCommand(
				server = server,
				stock_symbol = user_command['symbol'],
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.SET_BUY_TRIGGER:
			transaction = SetBuyTriggerCommand(
				server = server,
				stock_symbol = user_command['symbol'],
				amount = user_command['amount'],
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.SET_SELL_AMOUNT:
			transaction = SetSellAmountCommand(
				server = server,
				stock_symbol = user_command['symbol'],
				amount = user_command['amount'],
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.SET_SELL_TRIGGER:
			transaction = SetSellTriggerCommand(
				server = server,
				stock_symbol = user_command['symbol'],
				amount = user_command['amount'],
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.CANCEL_SET_SELL:
			transaction = CancelSetSellCommand(
				server = server,
				stock_symbol = user_command['symbol'],
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.DUMPLOG:
			transaction = CancelSetBuyCommand(
				server = server,
				user_account = user_account
			)
			transaction.save()
		elif user_command['command'] == Transaction.Command.DISPLAY_SUMMARY:
			transaction = CancelSetBuyCommand(
				server = server,
				user_account = user_account
			)
			transaction.save()

	return HttpResponse("Successfully ran workload.")
