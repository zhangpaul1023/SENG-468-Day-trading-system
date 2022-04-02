from django.core.management import BaseCommand
from transactions.models import *

class Command(BaseCommand):
	help = "check and set off triggers"

	def handle(self, *args, **options):
		buys = SetBuy.objects.all()
		sells = SetSell.objects.all()
		for trigger in buys: 
			if trigger.check_trigger():
				trigger.commit()
		for trigger in sells: 
			if trigger.check_trigger():
				trigger.commit()
