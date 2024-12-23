from celery import shared_task
from django.core.management import call_command


@shared_task
def update_tanks_db():
    call_command('1_get_tanks_from_tankopedia')
    return "Aktualizacja bazy danych z czołgami!!!"