from http.client import HTTPResponse
from pydoc import ModuleScanner
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from transactions.models import Transaction

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

	workload_transactions = []
	for user_command in workload_data:
		transaction = Transaction(
				server = gethostname(),
				command = user_command['command'],
		)
		workload_transactions.append(transaction)
	Transaction.objects.bulk_create(workload_transactions)
	return HttpResponse("Successfully ran workload.")
