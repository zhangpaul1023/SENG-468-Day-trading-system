from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command # NEW

logger = get_task_logger(__name__)

@shared_task
def sample_task():
    logger.info("The sample task just ran.")


# NEW
@shared_task
def check_triggers():
    call_command("check_triggers", )