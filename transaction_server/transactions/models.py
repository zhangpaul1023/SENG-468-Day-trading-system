from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


class User(models.Model):
	userid = models.CharField(max_length=50)
	funds = models.IntegerField()

class UncommittedBuy(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=50)
	funds = models.IntegerField()
	timestamp = models.DateTimeField()

# Create your models here.
class Event(models.Model):
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
	
	class Author(models.TextChoices):
		SYSTEM = 'SYSTEM'
		USER = 'USER'

	event_type = models.CharField(choices=Author.choices, max_length=6)
	transaction_number = models.AutoField(primary_key=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	server = models.CharField(max_length=64)
	command = models.CharField(choices=Command.choices, max_length=16)

class AddCommand(Event):
	command = Event.Command.ADD
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.DecimalField(decimal_places=2, max_digits=24)

class QuoteCommand(Event):
	command = Event.Command.QUOTE
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)

class BuyCommand(Event):
	command = Event.Command.BUY
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	amount = models.DecimalField(decimal_places=2, max_digits=24)
class SellCommand(Event):
	command = Event.Command.SELL
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	amount = models.DecimalField(decimal_places=2, max_digits=24)

class CommitBuyCommand(Event):
	command = Event.Command.COMMIT_BUY
	user = models.ForeignKey(User, on_delete=models.CASCADE)
class CommitSellCommand(Event):
	command = Event.Command.COMMIT_SELL
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class CancelBuyCommand(Event):
	command = Event.Command.CANCEL_BUY
	user = models.ForeignKey(User, on_delete=models.CASCADE)
class CancelSellCommand(Event):
	command = Event.Command.CANCEL_SELL
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class SetBuyAmountCommand(Event):
	command = Event.Command.SET_BUY_AMOUNT
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	amount = models.DecimalField(decimal_places=2, max_digits=24)
class SetSellAmountCommand(Event):
	command = Event.Command.SET_SELL_AMOUNT
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	amount = models.DecimalField(decimal_places=2, max_digits=24)

class CancelSetBuyCommand(Event):
	command = Event.Command.CANCEL_BUY
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
class CancelSetSellCommand(Event):
	command = Event.Command.CANCEL_SELL
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)

class SetBuyTriggerCommand(Event):
	command = Event.Command.SET_BUY_TRIGGER
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	amount = models.DecimalField(decimal_places=2, max_digits=24)
class SetSellTriggerCommand(Event):
	command = Event.Command.SET_SELL_TRIGGER
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	amount = models.DecimalField(decimal_places=2, max_digits=24)

class DumplogCommand(Event):
	command = Event.Command.DUMPLOG
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	filename = models.CharField(max_length=64, null=True)

class DisplaySummaryCommand(Event):
	command = Event.Command.DISPLAY_SUMMARY
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class AccountTransaction(models.Model):
	class Action(models.TextChoices):
		ADD = 'ADD'
		REMOVE = 'REMOVE'
	
	transaction_number = models.AutoField(primary_key=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	server = models.CharField(max_length=64)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	actions = models.CharField(choices=Action.choices, max_length=6)
	funds = models.DecimalField(decimal_places=2, max_digits=24)
