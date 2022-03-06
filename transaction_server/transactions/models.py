from argparse import ONE_OR_MORE
from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
	account_name = models.CharField(max_length=32)
	cumulative_funds = models.DecimalField(decimal_places=2, max_digits=24)

# Every command must be associated with a transactions.
# There is a 1:1 relationship between transactions and commands.
# Each transaction may create multiple system Transactions.


class Transaction(models.Model):
	class Command(models.TextChoices):
		ADD = 'ADD'
		QUOTE = 'QUOTE'
		BUY = 'BUY'
		COMMIT_BUY = 'COMMIT_BUY'
		CANCEL_BUY = 'CANCEL_BUY'
		SELL = 'SELL'
		COMMIT_SELL = 'COMMIT_SELL'
		CANCEL_SELL = 'CANCEL_SELL'
		SET_BUY_AMOUNT = 'SET_BUY_AMOUNT'
		CANCEL_SET_BUY = 'CANCEL_SET_BUY'
		SET_BUY_TRIGGER = 'SET_BUY_TRIGGER'
		SET_SELL_AMOUNT = 'SET_SELL_AMOUNT'
		SET_SELL_TRIGGER = 'SET_SELL_TRIGGER'
		CANCEL_SET_SELL = 'CANCEL_SET_SELL'
		DUMPLOG = 'DUMPLOG'
		DISPLAY_SUMMARY = 'DISPLAY_SUMMARY'

	timestamp = models.DateTimeField(auto_now_add=True)
	server = models.CharField(max_length=64)
	command = models.CharField(choices=Command.choices, max_length=16)
	quoteServerTime = models.DecimalField(decimal_places=2, max_digits=24, null=True)
	cryptokey = models.CharField(max_length=64, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=24, null=True)
	# Context-Dependant Fields
	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	amount = models.DecimalField(decimal_places=2, max_digits=24, null=True)
	filename = models.CharField(max_length=64, null=True)

class AccountTransaction(models.Model):
	class Action(models.TextChoices):
		ADD = 'ADD'
		REMOVE = 'REMOVE'
	
	transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE, primary_key=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	server = models.CharField(max_length=64)
	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
	actions = models.CharField(choices=Action.choices, max_length=6)
	funds = models.DecimalField(decimal_places=2, max_digits=24)

class LogEvent(models.Model):
	class EventType(models.TextChoices):
		SYSTEM = 'SYSTEM'
		ERROR = 'ERROR'
		DEBUG = 'DEBUG'
	class EventSource(models.TextChoices):
		USER_COMMAND = 'USER_COMMAND'
		INTERSERVER_COMMUNIATION = 'INTERSERVER_COMMUNICATION'
		TRIGGER_EXECUTION = 'TRIGGER_EXECUTION'
	transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
	event_type = models.CharField(choices=EventType.choices, max_length=6)
	event_source = models.CharField(choices=EventSource.choices, max_length=25)
	message = models.CharField(max_length=512, null=True)
