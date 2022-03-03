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
	
	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	amount = models.DecimalField(decimal_places=2, max_digits=24, null=True)

# class AddCommand(Transaction):
# 	command = Transaction.Command.ADD
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# 	amount = models.DecimalField(decimal_places=2, max_digits=24)

# class QuoteCommand(Transaction):
# 	command = Transaction.Command.QUOTE
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# 	stock_symbol = models.CharField(max_length=3, null=True)

# class BuyCommand(Transaction):
# 	command = Transaction.Command.BUY
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# 	stock_symbol = models.CharField(max_length=3, null=True)
# 	amount = models.DecimalField(decimal_places=2, max_digits=24)
# class SellCommand(Transaction):
# 	command = Transaction.Command.SELL
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# 	stock_symbol = models.CharField(max_length=3, null=True)
# 	amount = models.DecimalField(decimal_places=2, max_digits=24)

# class CommitBuyCommand(Transaction):
# 	command = Transaction.Command.COMMIT_BUY
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# class CommitSellCommand(Transaction):
# 	command = Transaction.Command.COMMIT_SELL
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

# class CancelBuyCommand(Transaction):
# 	command = Transaction.Command.CANCEL_BUY
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# class CancelSellCommand(Transaction):
# 	command = Transaction.Command.CANCEL_SELL
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

# class SetBuyAmountCommand(Transaction):
# 	command = Transaction.Command.SET_BUY_AMOUNT
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# 	stock_symbol = models.CharField(max_length=3, null=True)
# 	amount = models.DecimalField(decimal_places=2, max_digits=24)
# class SetSellAmountCommand(Transaction):
# 	command = Transaction.Command.SET_SELL_AMOUNT
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# 	stock_symbol = models.CharField(max_length=3, null=True)
# 	amount = models.DecimalField(decimal_places=2, max_digits=24)

# class CancelSetBuyCommand(Transaction):
# 	command = Transaction.Command.CANCEL_BUY
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# 	stock_symbol = models.CharField(max_length=3, null=True)
# class CancelSetSellCommand(Transaction):
# 	command = Transaction.Command.CANCEL_SELL
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# 	stock_symbol = models.CharField(max_length=3, null=True)

# class SetBuyTriggerCommand(Transaction):
# 	command = Transaction.Command.SET_BUY_TRIGGER
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# 	stock_symbol = models.CharField(max_length=3, null=True)
# 	amount = models.DecimalField(decimal_places=2, max_digits=24)
# class SetSellTriggerCommand(Transaction):
# 	command = Transaction.Command.SET_SELL_TRIGGER
# 	user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
# 	stock_symbol = models.CharField(max_length=3, null=True)
# 	amount = models.DecimalField(decimal_places=2, max_digits=24)

# class DumplogCommand(Transaction):
# 	command = Transaction.Command.DUMPLOG
# 	user_account = models.ForeignKey(UserAccount, null=True, on_delete=models.CASCADE)
# 	filename = models.CharField(max_length=64, null=True)

# class DisplaySummaryCommand(Transaction):
# 	command = Transaction.Command.DISPLAY_SUMMARY
# 	user_account = models.ForeignKey(UserAccount, null=True, on_delete=models.CASCADE)

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

class SystemEvent(models.Model):
	transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)

class ErrorEvent(models.Model):
	transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
	error_message = models.CharField(max_length=512)

class DebugEvent(models.Model):
	transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
	debug_message = models.CharField(max_length=512)