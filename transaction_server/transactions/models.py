from django.db import models
# from django.contrib.auth.models import User
from django.db.models.signals import pre_init
from django.dispatch import receiver
from django.conf import settings
from datetime import *
from decimal import *
import redis
import socket
from socket import gethostname

redis_instance = redis.StrictRedis(
	host=settings.REDIS_HOST,
	port=settings.REDIS_PORT,
	db=0,
	decode_responses=True
)

def cancel_if_not_none(item):
	if item != None: item.cancel()

class User(models.Model):
	userid = models.CharField(max_length=64)
	funds = models.DecimalField(decimal_places=2, max_digits=24, default=Decimal(0.0))

	def add_funds(self, amount):
		self.funds += amount
		self.save()
		AccountTransactionLog(server=gethostname(), user=self, actions='ADD', funds=amount).save()
	
	def remove_funds(self, amount):
		self.funds -= amount
		self.save()
		AccountTransactionLog(server=gethostname(), user=self, actions='REMOVE', funds=amount).save()

	def get_quote(self, stock_symbol):
		
		cached_quote = redis_instance.get(stock_symbol)
		if cached_quote != None:
			data = cached_quote.split(",")
			price = Decimal(data[0])
			quoteServerTime = int(data[3])
			cryptokey = data[4]
			QuoteServerLog(
				server=gethostname(),
				user=self,
				stock_symbol=stock_symbol,
				price=price,
				quoteServerTime=quoteServerTime,
				cryptokey=cryptokey,
			)
			return price

		HOST = settings.QUOTE_SERVER_HOST
		PORT = int(settings.QUOTE_SERVER_PORT)
		dataSend = str(self.userid) + " " + str(stock_symbol) + "\n"
		dataSend = bytes(dataSend, 'utf-8')
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
			s.connect((HOST, PORT))
			s.sendall(dataSend)
			data = s.recv(1024)

		receivedData = repr(data)
		receivedData = receivedData[1:].replace("'", "")
		data = receivedData.split(",")
		price = Decimal(data[0])
		quoteServerTime = int(data[3])
		cryptokey = data[4]
		redis_instance.set(stock_symbol, receivedData, ex=30)
		QuoteServerLog(	server=gethostname(),
						user=self,
						price=price,
						stock_symbol=stock_symbol,
						quoteServerTime=quoteServerTime,
						cryptokey=cryptokey).save()
		return price

	def get_stock_account(self, stock_symbol):
		try:
			stock_account = StockAccount.objects.get(user=self,stock_symbol=stock_symbol)
		except StockAccount.DoesNotExist:
			stock_account = StockAccount(user=self,stock_symbol=stock_symbol)
		return stock_account

	def get_recent_buy(self):
		recent = None
		try:
			recent = UncommittedBuy.objects.get(user=self)
		except UncommittedBuy.DoesNotExist:
			pass
		return recent

	def get_recent_sell(self):
		recent = None
		try:
			recent = UncommittedSell.objects.get(user=self)
		except UncommittedSell.DoesNotExist:
			pass
		return recent

	def get_set_buy(self, stock_symbol):
		set = None
		try:
			set = SetBuy.objects.get(user=self, stock_symbol=stock_symbol)
		except SetBuy.DoesNotExist:
			pass
		return set

	def get_set_sell(self, stock_symbol):
		set = None
		try:
			set = SetSell.objects.get(user=self, stock_symbol=stock_symbol)
		except SetSell.DoesNotExist:
			pass
		return set
	def dumplog(self):
		my_str = ''
		for log in UserCommandLog.objects.filter(user=user):
			my_str += str(log)
		for log in QuoteServerLog.objects.filter(user=user):
			my_str += str(log)
		for log in AccountTransactionLog.objects.filter(user=user):
			my_str += str(log)
		for log in SystemEventLog.objects.filter(user=user):
			my_str += str(log)
		for log in ErrorEventLog.objects.filter(user=user):
			my_str += str(log)
		return my_str

class StockAccount(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3)
	funds = models.DecimalField(decimal_places=2, max_digits=24, default=Decimal(0.0))

	def get_funds(self):
		return self.funds*self.user.get_quote(self.stock_symbol)
	def add_funds(self, amount):
		self.funds += amount/self.user.get_quote(self.stock_symbol)
		self.save()
	def remove_funds(self, amount):
		self.funds -= amount/self.user.get_quote(self.stock_symbol)
		self.save()

class UncomittedTransaction(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	funds = models.DecimalField(decimal_places=2, max_digits=24, default=Decimal(0.0))
	timestamp = models.DateTimeField(auto_now=True)
	
	def is_recent(self):
		return (self.timestamp - datetime.now(timezone.utc)).total_seconds() < 60

class UncommittedBuy(UncomittedTransaction):
	@classmethod
	def create(cls, user, stock_symbol, funds):
		cancel_if_not_none(user.get_recent_buy())
		user.remove_funds(funds)
		buy = UncommittedBuy(user=user, stock_symbol=stock_symbol, funds=funds)
		buy.save()
		return buy

	def commit(self):
		self.user.get_stock_account(self.stock_symbol).add_funds(self.funds)
		self.delete()
	def cancel(self):
		self.user.add_funds(self.funds)
		self.delete()

class UncommittedSell(UncomittedTransaction):
	@classmethod
	def create(cls, user, stock_symbol, funds):
		cancel_if_not_none(user.get_recent_sell())
		user.get_stock_account(stock_symbol).remove_funds(funds)
		sell = UncommittedSell(user=user, stock_symbol=stock_symbol, funds=funds)
		sell.save()
		return sell

	def commit(self):
		self.user.add_funds(self.funds)
		self.delete()
	def cancel(self):
		self.user.get_stock_account(self.stock_symbol).add_funds(self.funds)
		self.delete()

class SetTransaction(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stock_symbol = models.CharField(max_length=3, null=True)
	funds = models.DecimalField(decimal_places=2, max_digits=24)
	triggerAmount = models.DecimalField(decimal_places=2, max_digits=24, null=True)

	def set_trigger(self, amount):
		self.triggerAmount = amount
		self.save()

class SetBuy(SetTransaction):
	@classmethod
	def create(cls, user, stock_symbol, funds):
		cancel_if_not_none(user.get_set_buy(stock_symbol))
		user.remove_funds(funds)
		buy = SetBuy(user=user, stock_symbol=stock_symbol, funds=funds)
		buy.save()
		return buy
	def check_trigger(self):
		return self.triggerAmount != None and self.user.get_stock_account(self.stock_symbol).get_funds() <= self.triggerAmount
	def commit(self):
		UncommittedBuy.create(user=self.user,stock_symbol=self.stock_symbol,funds=self.funds).commit()
		SystemEventLog(server=gethostname(),user=self.user,command='SET_BUY_TRIGGER',stock_symbol=self.stock_symbol,funds=self.funds).save()
		self.delete()
	def cancel(self):
		self.user.add_funds(self.funds)
		self.delete()

class SetSell(SetTransaction):
	@classmethod
	def create(cls, user, stock_symbol, funds):
		cancel_if_not_none(user.get_set_sell(stock_symbol))
		user.get_stock_account(stock_symbol).remove_funds(funds)
		sell = SetSell(user=user, stock_symbol=stock_symbol, funds=funds)
		sell.save()
		return sell
	def check_trigger(self):
		return self.triggerAmount != None and self.user.get_stock_account(self.stock_symbol).get_funds() >= self.triggerAmount
	def commit(self):
		UncommittedSell.create(user=self.user,stock_symbol=self.stock_symbol,funds=self.funds).commit()
		SystemEventLog(server=gethostname(),user=self.user,command='SET_SELL_TRIGGER',stock_symbol=self.stock_symbol,funds=self.funds).save()
		self.delete()
	def cancel(self):
		self.user.get_stock_account(self.stock_symbol).add_funds(self.funds)
		self.delete()

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
class Action(models.TextChoices):
		ADD = 'ADD'
		REMOVE = 'REMOVE'
class Log(models.Model):
	timestamp = models.DateTimeField(auto_now=True)
	server = models.CharField(max_length=64)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	command = models.CharField(choices=Command.choices, max_length=16, null=True)
	stock_symbol = models.CharField(max_length=3, null=True)
	filename = models.CharField(max_length=64, null=True)
	funds = models.DecimalField(decimal_places=2, max_digits=24, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=24, null=True)
	quoteServerTime = models.DecimalField(decimal_places=0, max_digits=24, null=True)
	cryptokey = models.CharField(max_length=64, null=True)
	actions = models.CharField(choices=Action.choices, max_length=6)
	error_message = models.CharField(max_length=64, null=True)
	def __str__(self):
		my_str = ''
		my_str += '<transactionNum>0</transactionNum>'
		if self.timestamp != None:
			my_str += '<timestamp>{}</timestamp>'.format(self.timestamp.microsecond)
		if self.server != None:
			my_str +=  '<server>{}</server>'.format(self.server)
		if self.command != None:
			my_str +=  '<command>{}</command>'.format(self.command)
		if self.user.userid != None:
			my_str +=  '<username>{}</username>'.format(self.user.userid)
		if self.price != None:
			my_str +=  '<price>{}</price>'.format(self.price)
		if self.stock_symbol != None:
			my_str +=  '<stockSymbol>{}</stockSymbol>'.format(self.stock_symbol)
		if self.quoteServerTime != None:
			my_str +=  '<quoteServerTime>{}</quoteServerTime>'.format(self.quoteServerTime)
		if self.cryptokey != None:
			my_str +=  '<cryptokey>{}</cryptokey>'.format(self.cryptokey)
		if self.actions != None:
			my_str += '<action>{}</action>'.format(self.actions)
		if self.error_message != None:
			my_str +=  '<errorMessage>{}</errorMessage>'.format(self.error_message)
		if self.filename != None:
			my_str +=  '<filename>{}</filename>'.format(self.filename)
		if self.funds != None:
			my_str +=  '<funds>{}</funds>'.format(self.funds)

		return my_str

class UserCommandLog(Log):
        def __str__(self):
            return '<userCommand>' + super().__str__() + '</userCommand>'

class QuoteServerLog(Log):
        def __str__(self):
            return '<quoteServer>' + super().__str__() + '</quoteServer>'

class AccountTransactionLog(Log):
        def __str__(self):
            return '<accountTransaction>' + super().__str__() + '</accountTransaction>'

class SystemEventLog(Log):
        def __str__(self):
            return '<systemEvent>' + super().__str__() + '</systemEvent>'

class ErrorEventLog(Log):
        def __str__(self):
            return '<errorEvent>' + super().__str__() + '</errorEvent>'
