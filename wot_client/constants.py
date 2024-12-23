from server.local_settings import WOT_APP_ID

URL_PLAYERS = f"https://api-modernarmor.worldoftanks.com/wotx/account/list/?application_id={WOT_APP_ID}&search="
URL_VEHICLES = f"https://api-modernarmor.worldoftanks.com/wotx/encyclopedia/vehicles/?application_id={WOT_APP_ID}"
URL_PLAYER_VEHICLES = f"https://api-modernarmor.worldoftanks.com/wotx/tanks/stats/?application_id={WOT_APP_ID}&fields=tank_id%2C+all"
URL_TANK_STATS = f"https://api-modernarmor.worldoftanks.com/wotx/tanks/stats/?application_id={WOT_APP_ID}"
