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
    heavyTank = "Czołg ciężki",
    AT_SPG = "Niszczyciel czołgów",
    mediumTank = "Czołg średni",
    lightTank = "Czołg lekki",
    SPG = "Artyleria"

class Nation(TextChoices):
    italy = "Włochy",
    usa = "U.S.A.",
    czech = "Czecho-Słowacja",
    poland = "Polska",
    france = "France",
    sweden = "Szwecja",
    ussr = "Z.S.S.R.",
    china = "Chiny",
    uk = "Wielka Brytania",
    japan = "Japonia",
    merc = "Najemnicy",
    germany = "Niemcy",
