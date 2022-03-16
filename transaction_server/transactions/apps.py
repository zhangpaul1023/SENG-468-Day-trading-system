from django.apps import AppConfig
from django.db.models.signals import pre_save

class TransactionsConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'transactions'

	def ready(self):
		from . import signals
		pre_save.connect(signals.log_transaction)
