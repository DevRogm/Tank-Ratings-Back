from django.core.management.base import BaseCommand
from wot_client.services import WotClient


class Command(BaseCommand):
    help = 'Retrieves player id from the '

    def add_arguments(self, parser):
        parser.add_argument(
            '--nick',
            type=str,
        )
        parser.add_argument(
            '--console',
            type=str,
        )

    def handle(self, *args, **kwargs):
        try:
            wot_client = WotClient()
            json_data = wot_client.get_player_id_by_nick_and_console(nick=kwargs['nick'], console=kwargs['console'])
        except Exception as error:
            self.stdout.write(self.style.ERROR(f"Error message: {error}"))
            self.stdout.write(self.style.ERROR('Retrieving player id failed'))
            return
        self.stdout.write(self.style.SUCCESS('Retrieving player id successful'))
