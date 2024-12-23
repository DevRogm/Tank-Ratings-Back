import datetime
from urllib.parse import uses_relative

import pytz
from celery import shared_task
from django.core.management import call_command

from accounts.models import WotPlayer, ActivateAccount
from server.settings import TIME_ZONE
from wot_client.services import WotClient


@shared_task
def activate_account():
    wot_client = WotClient()
    accounts_to_activate = ActivateAccount.objects.all()
    for account in accounts_to_activate:
        tank_last_battle_unix_time = wot_client.get_tank_last_battle_time(tank_id=account.tank_id_to_activate, account_id=account.wot_account_id)
        start_time = account.time_to_activate - datetime.timedelta(minutes=30)
        end_time_unix = int(account.time_to_activate.timestamp())
        start_time_unix = int(start_time.timestamp())
        if start_time_unix <= tank_last_battle_unix_time <= end_time_unix:
            print("Udało się")
            wot_player = WotPlayer(user=account.user, wot_account_id=account.wot_account_id, nick=account.nick, console=account.console, is_active=True, activated_at=datetime.datetime.now(tz=pytz.timezone(TIME_ZONE)))
            wot_player.save()
            call_command("3_get_player_tanks", wot_player_id=wot_player.wot_account_id)
            account.delete()
        if int(datetime.datetime.now(tz=pytz.timezone(TIME_ZONE)).timestamp()) > end_time_unix:
            print("Nie udało się")
            account.delete()
    return "Sprawdzanie czy można aktywować konta użytkowników"


@shared_task
def update_players_tank():
    # Dorobić tutaj sprawdzenie kiedy gracz zagrał ostatnia bitwe i jesli w ciagu np 10 min. to aktualizować tylko dla tych graczy ktorzy cos zagrali.
    wot_players_id = WotPlayer.objects.all()
    for player_id in wot_players_id:
        try:
            wot_player_id = player_id.wot_account_id
            call_command("3_get_player_tanks", wot_player_id=wot_player_id)
        except Exception as error:
            print("update_players_tank error", error)
    return "Aktualizacja czołgów graczy z minimalną liczbą bitew!!!"