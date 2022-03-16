from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions.models import Transaction, LogEvent

@receiver(post_save, sender=Transaction)
def log_transaction(sender, **kwargs):
	created = kwargs.get('created')
	instance = kwargs.get('instance')
	if created and not hasattr(instance, 'systemevent'):
		system_event = LogEvent(
			transaction = instance,
			event_type = LogEvent.EventType.SYSTEM,
			event_source = LogEvent.EventSource.USER_COMMAND,
		)
		system_event.save()
