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



def create_user(request, userid):
	User(userid=userid).save()
	return HttpResponse("success")

def add(request, userid, amount):
	user = User.objects.get(userid=userid)
	user.add(amount)
	return HttpResponse("success")

def buy(request, userid, stock_symbol, amount):
	return HttpResponse("success")

def sell(request, userid, stock_symbol, amount):
	return HttpResponse("success")

def commit_buy(request, userid):
	return HttpResponse("success")

def commit_sell(request, userid):
	return HttpResponse("success")

def cancel_buy(request, userid):
	return HttpResponse("success")

def cancel_sell(request, userid):
	return HttpResponse("success")

def set_buy_amount(request, userid, stock_symbol, amount):
	return HttpResponse("success")

def set_buy_trigger(request, userid, stock_symbol, amount):
	return HttpResponse("success")

def cancel_set_buy(request, userid, stock_symbol):
	return HttpResponse("success")

def set_sell_amount(request, userid, stock_symbol, amount):
	return HttpResponse("success")

def set_sell_trigger(request, userid, stock_symbol, amount):
	return HttpResponse("success")

def cancel_set_sell(request, userid, stock_symbol):
	return HttpResponse("success")
