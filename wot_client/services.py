from re import search

import requests

from server.local_settings import WOT_APP_ID

class WotClient:
    def __init__(self):
        self.url_players = f"https://api-modernarmor.worldoftanks.com/wotx/account/list/?application_id={WOT_APP_ID}&search="
        self.url_vehicles = f"https://api-modernarmor.worldoftanks.com/wotx/encyclopedia/vehicles/?application_id={WOT_APP_ID}"
        self.url_players_vehicles = f"https://api-modernarmor.worldoftanks.com/wotx/tanks/stats/?application_id={WOT_APP_ID}"

    def get_tanks_from_tankopedia(self, **kwargs):
        """
        Method gets all tanks from API and save them in DB
        """
        try:
            response = requests.get(self.url_vehicles, params=kwargs)
            if response.status_code == 200:
                data = response.json()
                return data.get('data')
            else:
                print(f"Error: {response.status_code}")
                return
        except Exception as error:
            print(f"get_tanks_from_tankopedia error: {error}")
            raise Exception(error)

     # TODO: In the future add general params for all tanks (Vehicle characteristics tab)
    # def add_general_params(self):

    def get_player_id_by_nick_and_console(self, nick, console):
        """Method gets player id by nick and console"""
        full_nick = f"{nick}-{console}"
        try:
            print(self.url_players_vehicles+full_nick)
            response = requests.get(self.url_players+full_nick)
            if response.status_code == 200:
                data = response.json()
                return data.get('data')
            else:
                print(f"Error: {response.status_code}")
                return
        except Exception as error:
            print(f"get_player_id_by_nick_and_console error: {error}")
            raise Exception(error)

