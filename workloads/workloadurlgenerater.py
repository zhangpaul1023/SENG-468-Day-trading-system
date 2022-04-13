import argparse
import sys
import re
import json
import requests


f = open("final_workload_2019.txt", "r")
url = ""
for line in f:
    singleUrl = ""
    index = re.search("\[.*\]", line)
    string = line.replace(" ", "").replace("\n", "").replace(" ", "").replace(str(index[0]), "")
    command = string.split(",")
    if command[0] == 'ADD':
        singleUrl = "http://localhost:8000/transactions/add/" + command[1] + "/" + command[2] + "/"
    elif command[0] in ('BUY', 'SELL', 'SET_BUY_AMOUNT', 'SET_SELL_AMOUNT'):
        singleUrl = "http://localhost:8000/transactions/" + command[0].lower() + "/" + command[1] + "/" + command[2] + "/" + command[3] + "/"
    elif command[0] in ('QUOTE', 'CANCEL_SET_BUY', 'CANCEL_SET_SELL'):
        singleUrl = "http://localhost:8000/transactions/" + command[0].lower() + "/" + command[1] + "/" + command[2] + "/"
    elif command[0] in ('COMMIT_BUY', 'CANCEL_BUY', 'COMMIT_SELL', 'CANCEL_SELL', 'DISPLAY_SUMMARY'):
        singleUrl = "http://localhost:8000/transactions/" + command[0].lower() + "/" + command[1] + "/"
    elif command[0] in ('SET_BUY_TRIGGER', 'SET_SELL_TRIGGER'):
        singleUrl = "http://localhost:8000/transactions/" + command[0].lower() + "/" + command[1] + "/" + command[2] + "/" + command[3] + "/"
    elif command[0] == 'DUMPLOG' and len(command) == 1:
        singleUrl = "http://localhost:8000/transactions/dumplog" + command[1] + "/"
    url = url + singleUrl + "\n"
print (url)