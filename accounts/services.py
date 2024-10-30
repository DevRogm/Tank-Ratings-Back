from tanks.models import Tank
from .models import WotPlayer


class AccountService:

    def save_tank_with_min_battles(self, tanks_data, wot_account_id, num_of_battles):
        wot_player = WotPlayer.objects.get(wot_account_id=wot_account_id)
        tanks_with_min_battles = self._get_tanks_by_min_battles(tanks_data, num_of_battles, wot_account_id)
        try:
            tanks_objects = Tank.objects.filter(tank_id__in=tanks_with_min_battles)
            wot_player.available_tanks.set(tanks_objects)
        except Exception as error:
            print(f"save_tank_with_min_battles error: {error}")
            raise Exception(error)

    @staticmethod
    def _get_tanks_by_min_battles(tanks_data, num_of_battles, wot_account_id):
        tanks_id = []
        try:
            for tank in tanks_data[str(wot_account_id)]:
                if tank['all']['battles'] >= num_of_battles:
                    tanks_id.append(tank['tank_id'])
        except Exception as error:
            print(f"_get_tanks_by_min_battles error: {error}")
            raise Exception(error)
        return tanks_id
