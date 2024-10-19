from django.core.management.base import BaseCommand

from wot_client.services import WotClient


class Command(BaseCommand):
    help = 'Retrieves tank data from the API and saves it to the DB'

    def add_arguments(self, parser):
        parser.add_argument(
            '--tier',
            type=str,
            default='3,4,5,6,7,8,9,10',
        )
        parser.add_argument(
            '--fields',
            type=str,
            default='short_name, name, nation, is_premium, tier, era, tank_id, type, images',
        )
        parser.add_argument(
            '--limit',
            type=int,
        )

    def handle(self, *args, **kwargs):
        try:
            wot_client = WotClient()
            json_data = wot_client.get_tanks_from_tankopedia(tier=kwargs['tier'], fields=kwargs['fields'],
                                                             limit=kwargs.get('limit'))
        except Exception as error:
            self.stdout.write(self.style.ERROR(f"Error message: {error}"))
            self.stdout.write(self.style.ERROR('Vehicle data updated failed'))
            return
        self.stdout.write(self.style.SUCCESS('Vehicle data updated successfully'))
