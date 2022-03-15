from django.core.management import BaseCommand
from transactions.models import *

class QuoteServer:
	def __init__(self):
		self.price = ""
		self.quoteServerTime = ""
		self.cryptokey = ""

	def connect_quote(self, userid, stock_symbol):
		HOST = '192.168.4.2'
		PORT = 4444
		dataSend = userid+stock_symbol+"\n"
		dataSend = str.encode(dataSend)
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
			s.connect((HOST, PORT))
			s.sendall(dataSend)
			data = s.recv(1024)

		receivedData = repr(data)
		receivedData = receivedData[1:].replace("'", "")
		data = receivedData.split(",")
		self.price = data[0]
		self.quoteServerTime = data[3]
		self.cryptokey = data[4]
	def get_price(self):
		return int(self.price)
	def get_quoteServerTime(self):
		return self.quoteServerTime
	def get_cryptokey(self):
		return self.cryptokey

class UserManager:
	def __init__(self, userid):
		self.user = User.objects.get(userid=userid)
	def add_funds(self, amount):
		self.user.funds += amount
		self.user.save()
	def get_funds(self):
		return self.user.funds
	def uncommit_buy(self, stock_symbol, amount):
		try:
			buy = UncommittedBuy.objects.get(user=self.user)
			buy.delete()
		except UncommittedBuy.DoesNotExist:
			pass
		buy = UncommittedBuy(user=self.user, stock_symbol=stock_symbol, funds=amount, timestamp=datetime.now())
		buy.save()
	
	def uncommit_sell(self, stock_symbol, amount):
		try:
			sell = UncommittedSell.objects.get(user=self.user)
			sell.delete()
		except UncommittedSell.DoesNotExist:
			pass
		sell = UncommittedSell(user=self.user, stock_symbol=stock_symbol, funds=amount, timestamp=datetime.now())
		sell.save()

	def has_recent_buy(self):
		try:
			buy = UncommittedBuy.objects.get(user=self.user)
			buy_timestamp = buy.timestamp
			current_time = datetime.now(timezone.utc)
			time_difference = current_time - buy_timestamp
			return time_difference.total_seconds() < 60
		except UncommittedBuy.DoesNotExist:
			return False

	def has_recent_sell(self):
		try:
			sell = UncommittedSell.objects.get(user=self.user)
			sell_timestamp = sell.timestamp
			current_time = datetime.now(timezone.utc)
			time_difference = current_time - sell_timestamp
			return time_difference.total_seconds() < 60
		except UncommittedSell.DoesNotExist:
			return False

	def create_buy_amount(self, stock_symbol, amount):
		buy = BuyTrigger(user=self.user,stock_symbol=stock_symbol,amount=amount,triggerAmount=0)
		buy.save()

	def set_buy_trigger(self, stock_symbol, amount):
		buy = BuyTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
		buy.triggerAmount = amount
		buy.save()

	def cancel_set_buy(self, stock_symbol):
		buy = BuyTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
		buy.delete()

	def create_sell_amount(self, stock_symbol, amount):
		sell = SellTrigger(user=self.user,stock_symbol=stock_symbol,amount=amount,triggerAmount=999999)
		sell.save()

	def set_sell_trigger(self, stock_symbol, amount):
		sell = SellTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
		sell.triggerAmount = amount
		sell.save()

	def cancel_set_buy(self, stock_symbol):
		sell = BuyTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
		sell.delete()

	def commit_buy(self):
		buy = UncommittedBuy.objects.get(user=self.user)
		try:
			stock_account = StockAccount.objects.get(user=self.user,stock_symbol=buy.stock_symbol)
		except StockAccount.DoesNotExist:
			stock_account = StockAccount(user=self.user,stock_symbol=buy.stock_symbol,amount=0)
		self.user.funds -= buy.funds
		self.user.save()
		quote_server = QuoteServer()
		quote = quote_server.get_price()
		stock_account.amount += (buy.funds * 100)/quote

		buy.delete()
		stock_account.save()

	def commit_sell(self):
		sell = UncommittedSell.objects.get(user=self.user)
		try:
			stock_account = StockAccount.objects.get(user=self.user,stock_symbol=sell.stock_symbol)
		except StockAccount.DoesNotExist:
			stock_account = StockAccount(user=self.user,stock_symbol=sell.stock_symbol,amount=0)
		self.user.funds += sell.funds
		self.user.save()
		quote_server = QuoteServer()
		quote = quote_server.get_price()
		stock_account.amount -= (sell.funds * 100)/quote

		sell.delete()
		stock_account.save()

	def cancel_buy(self):
		try:
			buy = UncommittedBuy.objects.get(user=self.user)
			buy.delete()
		except UncommittedBuy.DoesNotExist:
			pass

	def cancel_sell(self):
		try:
			sell = UncommittedSell.objects.get(user=self.user)
			sell.delete()
		except UncommittedSell.DoesNotExist:
			pass

	def stock(self, stock_symbol):
		try:
			stock_account = StockAccount.objects.get(user=self.user,stock_symbol=stock_symbol)
		except StockAccount.DoesNotExist:
			stock_account = StockAccount(user=self.user,stock_symbol=stock_symbol,amount=0)
		quote_server = QuoteServer()
		quote = quote_server.get_price()
		return stock_account.amount * quote

	def has_set_buy(self, stock_symbol):
		try:
			buy = BuyTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
			return True
		except BuyTrigger.DoesNotExist:
			return False

	def has_set_sell(self, stock_symbol):
		try:
			sell = SellTrigger.objects.get(user=self.user,stock_symbol=stock_symbol)
			return True
		except SellTrigger.DoesNotExist:
			return False



class Command(BaseCommand):
	help = "TODO"

	def handle(self, *args, **options):
		quote_server = QuoteServer()
		buys = BuyTrigger.objects.all()
		sells = SellTrigger.objects.all()
		
		for buy in buys:
			quote_server.connect_quote(buy.user, buy.stock_symbol)
			current_quote = quote_server.get_price()
			if (current_quote >= buy.triggerAmount):
				user = UserManager(buy.user)
				user.uncommit_buy(buy.stock_symbol, buy.amount)
				user.commit_buy()
				buy.delete()
		for sell in sells:
			quote_server.connect_quote(sell.user, sell.stock_symbol)
			current_quote = quote_server.get_price()
			if (current_quote <= sell.triggerAmount):
				user = UserManager(sell.user)
				user.uncommit_buy(sell.stock_symbol, sell.amount)
				user.commit_buy()
				sell.delete()



