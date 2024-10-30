from django.core.management.base import BaseCommand

from accounts.services import AccountService
from accounts.constants import MIN_NUM_OF_BATTLES
from wot_client.services import WotClient


class Command(BaseCommand):
    help = 'Get players tanks and save to the DB only those with a minimum number of battles of 50'

    def add_arguments(self, parser):
        parser.add_argument(
            '--wot_player_id',
            type=int,
        )

    def handle(self, *args, **kwargs):
        try:
            wot_client = WotClient()
            account_service = AccountService()
            json_data = wot_client.get_tank_stats_by_wot_player_id(account_id=kwargs['wot_player_id'])
            account_service.save_tank_with_min_battles(json_data, kwargs['wot_player_id'], MIN_NUM_OF_BATTLES)
        except Exception as error:
            self.stdout.write(self.style.ERROR(f"Error message: {error}"))
            self.stdout.write(self.style.ERROR('Failed to get players tank data'))
            return
        self.stdout.write(self.style.SUCCESS('Getting data about the players tanks was successful'))
