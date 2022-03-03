from django.db.models.signals import pre_save
from django.dispatch import receiver
from transactions.models import Transaction, SystemEvent

@receiver(pre_save, sender=Transaction)
def log_transaction(sender, instance, **kwargs):
	print("It's me, ya boi!")
	system_event = SystemEvent(transaction=instance.transaction)
	system_event.save()
