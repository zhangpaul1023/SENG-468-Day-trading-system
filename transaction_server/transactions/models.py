from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

class User(models.Model):
	userid = models.CharField(max_length=64)
	funds = models.DecimalField(decimal_places=2, max_digits=24)

	def add(self, amount):
		self.funds += amount
		self.save()
		AccountTransactionLog(server='this', user=self, actions=ADD, funds=amount).save()

class StockAccount(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	funds = models.DecimalField(decimal_places=2, max_digits=24)

class UncommittedBuy(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	funds = models.DecimalField(decimal_places=2, max_digits=24)
	timestamp = models.DateTimeField()

class UncommittedSell(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	funds = models.DecimalField(decimal_places=2, max_digits=24)
	timestamp = models.DateTimeField()

class BuyTrigger(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=50)
	funds = models.DecimalField(decimal_places=2, max_digits=24)
	triggerAmount = models.DecimalField(decimal_places=2, max_digits=24)

class SellTrigger(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=50)
	funds = models.DecimalField(decimal_places=2, max_digits=24)
	triggerAmount = models.DecimalField(decimal_places=2, max_digits=24)

# Create your models here.
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

class Log(models.Model):
	timestamp = models.DateTimeField(auto_now=False)
	server = models.CharField(max_length=64)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserCommandLog(Log):
	command = models.CharField(choices=Command.choices, max_length=16)
	stock_symbol = models.CharField(max_length=3, null=True)
	filename = models.CharField(max_length=64, null=True)
	funds = models.DecimalField(decimal_places=2, max_digits=24)

class QuoteServerLog(Log):
	price = models.DecimalField(decimal_places=2, max_digits=24, null=True)
	stock_symbol = models.CharField(max_length=3, null=True)
	quoteServerTime = models.DecimalField(decimal_places=0, max_digits=24, null=True)
	cryptokey = models.CharField(max_length=64, null=True)

class AccountTransactionLog(Log):
	class Action(models.TextChoices):
		ADD = 'ADD'
		REMOVE = 'REMOVE'
	actions = models.CharField(choices=Action.choices, max_length=6)
	funds = models.DecimalField(decimal_places=2, max_digits=24)

class SystemEventLog(Log):
	command = models.CharField(choices=Command.choices, max_length=16)
	stock_symbol = models.CharField(max_length=3, null=True)
	filename = models.CharField(max_length=64, null=True)
	funds = models.DecimalField(decimal_places=2, max_digits=24)

class ErrorEventLog(Log):
	command = models.CharField(choices=Command.choices, max_length=16)
	stock_symbol = models.CharField(max_length=3, null=True)
	filename = models.CharField(max_length=64, null=True)
	funds = models.DecimalField(decimal_places=2, max_digits=24)
	error_message = models.CharField(max_length=64, null=True)
