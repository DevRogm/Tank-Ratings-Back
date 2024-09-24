from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

class Tier(TextChoices):
    III = "III", _("III")
    IV = "IV", _("IV")
    V = "V", _("V")
    VI = "VI", _("VI")
    VII = "VII", _("VII")
    VIII = "VIII", _("VIII")
    IX = "IX", _("IX")
    X = "X", _("X")

class Type(TextChoices):
    light_tank = "Czołg lekki", _("Czołg lekki")
    medium_tank = "Czołg średni", _("Czołg średni")
    heavy_tank = "Czołg ciężki", _("Czołg ciężki")
    tank_destroyer = "Niszczyciel czołgów", _("Niszczyciel czołgów")
    artillery = "Artyleria", _("Artyleria")

class Nation(TextChoices):
    mercenaries  = "Najemnicy", _("Najemnicy")
    italy  = "Włochy", _("Włochy")
    poland  = "Polska", _("Polska")
    sweden  = "Szwecja", _("Szwecja")
    czechoslovakia  = "Czecho-Słowacja", _("Czecho-Słowacja")
    china  = "Chiny", _("Chiny")
    japan  = "Japan", _("Japan")
    france  = "France", _("France")
    ussr  = "Związek Radziecki", _("Związek Radziecki")
    uk  = "Wielka Brytania", _("Wielka Brytania")
    germany = "Niemcy", _("Niemcy")
    usa = "U.S.A", _("USA")