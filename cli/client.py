#!/usr/bin/env python3

import argparse
import sys
import re
import json
import requests

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='send workload file to server as json')
	parser.add_argument('input_file', metavar='input_file', help='a workload file')
	parser.add_argument('server', help='server to send workload to')

	file_name = parser.parse_args().input_file
	server_url = parser.parse_args().server

	lines = []
	try:
		lines = [line.rstrip('\n') for line in open(file_name)]
		lines = [re.sub(']\s', '],', line) for line in lines]
	except:
		sys.exit(
			'failed to parse workload file: {file_name}'.format(file_name))

	transactions = []
	for line_number, line in enumerate(lines):
		_, command, *parameters = line.split(',')

		transaction = {
			'command': command,
			'transactionNum': line_number + 1
		}
		if command == 'ADD':
			transaction.update({
				'userId': parameters[0],
				'amount': float(parameters[1])
			})
		elif command in ('BUY', 'SELL', 'SET_BUY_AMOUNT', 'SET_SELL_AMOUNT'):
			transaction.update({
				'userId': parameters[0],
				'symbol': parameters[1],
				'amount': float(parameters[2])
			})
		elif command in ('QUOTE', 'CANCEL_SET_BUY', 'CANCEL_SET_SELL'):
			transaction.update({
				'userId': parameters[0],
				'symbol': parameters[1]
			})
		elif command in ('COMMIT_BUY', 'CANCEL_BUY', 'COMMIT_SELL', 'CANCEL_SELL', 'DISPLAY_SUMMARY'):
			transaction.update({
				'userId': parameters[0]
			})
		elif command in ('SET_BUY_TRIGGER', 'SET_SELL_TRIGGER'):
			transaction.update({
				'userId': parameters[0],
				'symbol': parameters[1],
				'price': parameters[2]
			})
		elif command == 'DUMPLOG' and len(parameters) == 1:
			transaction.update({
				'filename': parameters[0]
			})
		else:
			sys.exit('invalid command on line: {line_number}'.format(line_number))

		transactions.append(transaction)
	
	request = requests.post(
		server_url,
		headers={'content-type': 'application/json'},
		data=json.dumps(transactions)
	)

	print('{}: {}'.format(request.status_code, request.text))