from django.db import models

# Create your models here.
class Transaction(models.Model):
	transactionNum = models.AutoField(primary_key=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	server = models.CharField(max_length=64)
	command = models.IntegerChoices('Place',
		'ADD'
		'QUOTE'

		'BUY'
		'COMMIT_BUY'
		'CANCEL_BUY'

		'SELL'
		'COMMIT_SELL'
		'CANCEL_SELL'

		'SET_BUY_AMOUNT'
		'CANCEL_SET_BUY'
		'SET_BUY_TRIGGER'

		'SET_SELL_AMOUNT'
		'SET_SELL_TRIGGER'
		'CANCEL_SET_SELL'

		'DUMPLOG'
		'DISPLAY_SUMMARY'
	)

	# Optional Fields
	username = models.CharField(max_length=64, null=True)
	stock_symbol = models.CharField(max_length=3, null=True)
	filename = models.CharField(max_length=64, null=True)
	funds = models.DecimalField(decimal_places=2, max_digits=24, null=True)
