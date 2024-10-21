from django.db import transaction

from .models import Tank


class TankService:
    def save_tanks_to_db(self, tanks_data):
        """
        Method saves tanks from API to db
        :param tanks_data:
        :return:
        """
        try:
            tanks = [Tank(short_name=tank_data['short_name'], name=tank_data['name'],
                          nation=tank_data['nation'], is_premium=tank_data['is_premium'],
                          tier=tank_data['tier'], era=tank_data['era'],
                          tank_id=tank_data['tank_id'], type=tank_data['type'], url_img=tank_data['images']['big_icon']
                          ) for tank_data in tanks_data.values()]

            existing_tanks = Tank.objects.filter(tank_id__in=[tank.tank_id for tank in tanks])
            existing_tanks_map = {tank.tank_id: tank for tank in existing_tanks}
            new_tanks = [tank for tank in tanks if tank.tank_id not in existing_tanks_map]
            with transaction.atomic():
                if new_tanks:
                    Tank.objects.bulk_create(new_tanks)
                if existing_tanks:
                    Tank.objects.bulk_update(existing_tanks,
                                             ['short_name', 'name', 'nation', 'is_premium', 'tier', 'era', 'tank_id',
                                              'type', 'url_img'])
            print(f"== INFO == Created tanks: {len(new_tanks)}")
            print(f"== INFO == Updated tanks: {len(existing_tanks_map)}")
        except Exception as error:
            print(f"save_tanks_to_db error: {error}")
            raise Exception(error)

        # short_name, name, nation, is_premium, tier, era, tank_id, type, images
