import requests

from wot_client.constants import URL_VEHICLES, URL_PLAYERS, URL_PLAYER_VEHICLES


class WotClient:

    @staticmethod
    def get_tanks_from_tankopedia(**kwargs):
        """
        Method gets all tanks from API and save them in DB
        """
        try:
            response = requests.get(URL_VEHICLES, params=kwargs)
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

    @staticmethod
    def get_player_id_by_nick_and_console(nick, console):
        """
        Method gets player id by nick and console
        """
        full_nick = f"{nick}-{console}"
        try:
            response = requests.get(URL_PLAYERS + full_nick)
            if response.status_code == 200:
                data = response.json()
                return data.get('data')
            else:
                print(f"Error: {response.status_code}")
                return
        except Exception as error:
            print(f"get_player_id_by_nick_and_console error: {error}")
            raise Exception(error)

    @staticmethod
    def get_tank_stats_by_wot_player_id(**kwargs):
        """
        Method gets all players tanks
        """
        try:
            response = requests.get(URL_PLAYER_VEHICLES, params=kwargs)
            if response.status_code == 200:
                data = response.json()
                return data.get('data')
            else:
                print(f"Error: {response.status_code}")
                return
        except Exception as error:
            print(f"get_player_id_by_nick_and_console error: {error}")
            raise Exception(error)
