from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseForbidden
from transactions.models import LogEvent, Transaction, UserAccount
import socket
from socket import gethostname
from json import loads

(
	ADD,
	QUOTE,
	BUY,
	COMMIT_BUY,
	CANCEL_BUY,
	SELL,
	COMMIT_SELL,
	CANCEL_SELL,
	SET_BUY_AMOUNT,
	CANCEL_SET_BUY,
	SET_BUY_TRIGGER,
	SET_SELL_AMOUNT,
	SET_SELL_TRIGGER,
	CANCEL_SET_SELL,
	DUMPLOG,
	DISPLAY_SUMMARY
) = Transaction.Command

# Create your views here.
@csrf_exempt
def index(request):
	return HttpResponse("This is the transaction server.")

def QuoteServer(userid, stock_symbol):
	returndata = []
	HOST = '192.168.4.2'
	PORT = 4444
	dataSend = str(userid) + " " + str(stock_symbol) + "\n"
	dataSend = bytes(dataSend, 'utf-8')
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
		s.connect((HOST, PORT))
		s.sendall(dataSend)
		data = s.recv(1024)

	receivedData = repr(data)
	receivedData = receivedData[1:].replace("'", "")
	data = receivedData.split(",")
	price = float(data[0])
	quoteServerTime = int(data[3])
	cryptokey = data[4]
	returndata.append(price)
	returndata.append(quoteServerTime)
	returndata.append(cryptokey)
	return (returndata)



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
	for command_data in workload_data:
		command = command_data['command']

		if command == DUMPLOG and not 'userId' in command_data:
			continue

		user_account = UserAccount.objects.filter(account_name=command_data['userId']).first()
		if user_account == None:
			return HttpResponseForbidden("Unable to access resources of user.")

		transaction = None

		if command == ADD:
			transaction = Transaction(
				server = server,
				command = command,
				amount = command_data['amount'],
				user_account = user_account
			)
		elif command in (BUY, SELL, SET_BUY_AMOUNT, SET_SELL_AMOUNT):
			transaction = Transaction(
				server = server,
				command = command,
				stock_symbol = command_data['symbol'],
				amount = command_data['amount'],
				user_account = user_account
			)
		elif command in (CANCEL_SET_BUY, CANCEL_SET_SELL):
			transaction = Transaction(
				server = server,
				command = command,
				stock_symbol = command_data['symbol'],
				user_account = user_account
			)
		elif command == QUOTE:
			transaction = Transaction(
				server=server,
				command=command,
				price=QuoteServer(user_account, command_data['symbol'])[0],
				quoteServerTime=int(QuoteServer(user_account, command_data['symbol'])[1]),
				cryptokey=QuoteServer(user_account, command_data['symbol'])[2],
				stock_symbol=command_data['symbol'],
				user_account=user_account
			)
		elif command in (COMMIT_BUY, CANCEL_BUY, COMMIT_SELL, CANCEL_SELL, DISPLAY_SUMMARY):
			transaction = Transaction(
				server = server,
				command = command,
				user_account = user_account
			)
		elif command in (SET_BUY_TRIGGER, SET_SELL_TRIGGER):
			transaction = Transaction(
				server = server,
				command = command,
				stock_symbol = command_data['symbol'],
				amount = command_data['amount'],
				user_account = user_account
			)
		elif command == DUMPLOG:
			transaction = Transaction(
				server = server,
				command = command,
				filename = command_data['filename']
			)
		else:
			return HttpResponseBadRequest("Malformed workload parameters.")

		transaction.save()

	log_events = LogEvent.objects.all()
	return render(request, 'transactions/workload.xml', {'log_events': log_events})
