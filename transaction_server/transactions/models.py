from django.db import models

# Create your models here.
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

	transactionNum = models.AutoField(primary_key=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	server = models.CharField(max_length=64)
	command = models.CharField(choices=Command.choices, max_length=16)

	# Optional Fields
	username = models.CharField(max_length=64, null=True)
	stock_symbol = models.CharField(max_length=3, null=True)
	filename = models.CharField(max_length=64, null=True)
	funds = models.DecimalField(decimal_places=2, max_digits=24, null=True)
