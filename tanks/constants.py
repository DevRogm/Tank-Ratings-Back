from django.db.models import TextChoices

class Tier(TextChoices):
    III = "III"
    IV = "IV"
    V = "V"
    VI = "VI"
    VII = "VII"
    VIII = "VIII"
    IX = "IX"
    X = "X",

class Type(TextChoices):
    light_tank = "Czołg lekki"
    medium_tank = "Czołg średni"
    heavy_tank = "Czołg ciężki"
    tank_destroyer = "Niszczyciel czołgów"
    artillery = "Artyleria"

class Nation(TextChoices):
    mercenaries  = "Najemnicy"
    italy  = "Włochy"
    poland  = "Polska"
    sweden  = "Szwecja"
    czechoslovakia  = "Czecho-Słowacja"
    china  = "Chiny"
    japan  = "Japan"
    france  = "France"
    ussr  = "Związek Radziecki"
    uk  = "Wielka Brytania"
    germany = "Niemcy"
    usa = "U.S.A"
