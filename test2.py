import sys
import re
import socket
import time

lines = [line.rstrip('\n') for line in open(sys.argv[1])]
lines = [re.sub(']\s', '],', line) for line in lines]

count = 0

for line in lines:
  count += 1
  commands = line.split(',')
  command_type = commands.pop(1)

  command_dict = {
    'transactionNum': count
  }
  if command_type == 'ADD':
    command_dict.update({
      'userID': commands[1],
      'amount': float(commands[2])
    })
  elif command_type in ('BUY', 'SELL', 'SET_BUY_AMOUNT', 'SET_SELL_AMOUNT'):
    command_dict.update({
      'userID': commands[1],
      'symbol': commands[2],
      'amount': float(commands[3])
    })
  elif command_type in ('QUOTE', 'CANCEL_SET_BUY', 'CANCEL_SET_SELL'):
    command_dict.update({
      'userID': commands[1],
      'symbol': commands[2]
    })
  elif command_type in ('COMMIT_BUY', 'CANCEL_BUY', 'COMMIT_SELL', 'CANCEL_SELL', 'DISPLAY_SUMMARY'):
    command_dict.update({
      'userID': commands[1]
    })

  elif command_type in ('SET_BUY_TRIGGER', 'SET_SELL_TRIGGER'):
    price = float(commands[3])
    command_dict.update({
      'userID': commands[1],
      'symbol': commands[2],
      'price': price
    })
  elif command_type == 'DUMPLOG' and len(commands) == 2:
    command_dict.update({
      'filename': commands[1]
    })

  time.sleep(0.005)
