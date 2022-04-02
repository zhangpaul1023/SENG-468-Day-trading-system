from django.core.management import BaseCommand
from transactions.models import *

class Command(BaseCommand):
	help = "check and set off triggers"

	def handle(self, *args, **options):
		triggers = SetTransaction.objects.all()
		for trigger in triggers: 
			if trigger.check_trigger():
				trigger.commit()