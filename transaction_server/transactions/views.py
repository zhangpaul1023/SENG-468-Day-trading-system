from http.client import HTTPResponse
from pydoc import ModuleScanner
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import socket
from socket import gethostname
from json import loads
from .models import *
from datetime import datetime, timezone
from decimal import *



def create_user(request, userid):
	User(userid=userid).save()
	return HttpResponse("success")

def add(request, userid, amount):
	user = User.objects.get(userid=userid)
	funds = Decimal(amount.replace(',','.'))
	user.add_funds(funds)
	UserCommandLog(server=gethostname(), user=user, command='ADD', funds=funds).save()
	return HttpResponse("success")

def quote(request, userid, stock_symbol):
	user = User.objects.get(userid=userid)
	UserCommandLog(server=gethostname(), user=user, command='QUOTE', stock_symbol=stock_symbol).save()
	return HttpResponse("{}".format(user.get_quote(stock_symbol)))

def buy(request, userid, stock_symbol, amount):
	user = User.objects.get(userid=userid)
	funds = Decimal(amount.replace(',','.'))
	if user.funds < funds:
		ErrorEventLog(server=gethostname(), user=user, command='BUY', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("failure")
	else:
		UncommittedBuy.create(user=user, stock_symbol=stock_symbol, funds=funds)
		UserCommandLog(server=gethostname(), user=user, command='BUY', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("success")

def sell(request, userid, stock_symbol, amount):
	user = User.objects.get(userid=userid)
	funds = Decimal(amount.replace(',','.'))
	if user.get_stock_account(stock_symbol).get_funds() < funds:
		ErrorEventLog(server=gethostname(), user=user, command='SELL', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("failure")
	else:
		UncommittedSell.create(user=user, stock_symbol=stock_symbol, funds=funds)
		UserCommandLog(server=gethostname(), user=user, command='SELL', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("success")

def commit_buy(request, userid):
	user = User.objects.get(userid=userid)
	buy = user.get_recent_buy()
	if buy == None or not buy.is_recent():
		ErrorEventLog(server=gethostname(), user=user, command='COMMIT_BUY').save()
		return HttpResponse("failure")
	else:
		buy.commit()
		UserCommandLog(server=gethostname(), user=user, command='COMMIT_BUY').save()
		return HttpResponse("success")

def commit_sell(request, userid):
	user = User.objects.get(userid=userid)
	sell = user.get_recent_sell()
	if sell == None or not sell.is_recent():
		ErrorEventLog(server=gethostname(), user=user, command='COMMIT_SELL').save()
		return HttpResponse("success")
	else:
		sell.commit()
		UserCommandLog(server=gethostname(), user=user, command='COMMIT_SELL').save()
		return HttpResponse("success")


def cancel_buy(request, userid):
	user = User.objects.get(userid=userid)
	buy = user.get_recent_buy()
	if buy == None:
		ErrorEventLog(server=gethostname(), user=user, command='CANCEL_BUY').save()
		return HttpResponse("failure")
	else:
		buy.cancel()
		UserCommandLog(server=gethostname(), user=user, command='CANCEL_BUY').save()
		return HttpResponse("success")

def cancel_sell(request, userid):
	user = User.objects.get(userid=userid)
	sell = User.get_recent_sell()
	if sell == None:
		ErrorEventLog(server=gethostname(), user=user, command='CANCEL_SELL').save()
		return HttpResponse("failure")
	else:
		sell.cancel()
		UserCommandLog(server=gethostname(), user=user, command='CANCEL_SELL').save()
		return HttpResponse("success")

def set_buy_amount(request, userid, stock_symbol, amount):
	user = User.objects.get(userid=userid)
	funds = Decimal(amount.replace(',','.'))
	if user.funds < funds:
		ErrorEventLog(server=gethostname(), user=user, command='SET_BUY_AMOUNT', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("failure")
	else:
		SetBuy.create(user=user, stock_symbol=stock_symbol, funds=funds)
		UserCommandLog(server=gethostname(), user=user, command='SET_BUY_AMOUNT', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("success")

def set_buy_trigger(request, userid, stock_symbol, amount):
	user = User.objects.get(userid=userid)
	buy = user.get_set_buy(stock_symbol)
	funds = Decimal(amount.replace(',','.'))
	if buy == None:
		ErrorEventLog(server=gethostname(), user=user, command='SET_BUY_TRIGGER', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("failure")
	else:
		buy.set_trigger(funds)
		UserCommandLog(server=gethostname(), user=user, command='SET_BUY_TRIGGER', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("success")

def cancel_set_buy(request, userid, stock_symbol):
	user = User.objects.get(userid=userid)
	buy = user.get_set_buy(stock_symbol)
	if buy == None:
		ErrorEventLog(server=gethostname(), user=user, command='CANCEL_SET_BUY', stock_symbol=stock_symbol).save()
		return HttpResponse("failure")
	else:
		buy.cancel()
		UserCommandLog(server=gethostname(), user=user, command='CANCEL_SET_BUY', stock_symbol=stock_symbol).save()
		return HttpResponse("success")

def set_sell_amount(request, userid, stock_symbol, amount):
	user = User.objects.get(userid=userid)
	funds = Decimal(amount.replace(',','.'))
	if user.get_stock_account(stock_symbol).get_funds() < funds:
		ErrorEventLog(server=gethostname(), user=user, command='SET_SELL_AMOUNT', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("failure")
	else:
		SetSell.create(user=user, stock_symbol=stock_symbol, funds=funds)
		UserCommandLog(server=gethostname(), user=user, command='SET_SELL_AMOUNT', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("success")

def set_sell_trigger(request, userid, stock_symbol, amount):
	user = User.objects.get(userid=userid)
	sell = user.get_set_sell(stock_symbol)
	funds = Decimal(amount.replace(',','.'))
	if sell == None:
		ErrorEventLog(server=gethostname(), user=user, command='SET_SELL_TRIGGER', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("failure")
	else:
		sell.set_trigger(funds)
		UserCommandLog(server=gethostname(), user=user, command='SET_SELL_TRIGGER', stock_symbol=stock_symbol, funds=funds).save()
		return HttpResponse("success")

def cancel_set_sell(request, userid, stock_symbol):
	user = User.objects.get(userid=userid)
	sell = user.get_set_sell(stock_symbol)
	if sell == None:
		ErrorEventLog(server=gethostname(), user=user, command='CANCEL_SET_SELL', stock_symbol=stock_symbol).save()
		return HttpResponse("failure")
	else:
		sell.cancel()
		UserCommandLog(server=gethostname(), user=user, command='CANCEL_SET_SELL', stock_symbol=stock_symbol).save()
		return HttpResponse("success")
