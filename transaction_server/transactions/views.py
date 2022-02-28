from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
	return HttpResponse("This is the transaction server.")

@csrf_exempt
def workload(request):
	if request.method != 'POST':
		return HttpResponseNotAllowed(['POST'])
	# if request.content_type != 'application/json':
	#	return HttpResponseBadRequest(request.content_type)

	
