from django.db.models import IntegerChoices

class RatingRange(IntegerChoices):
    I = 1, "1"
    II = 2, "2"
    III = 3, "3"
    IV = 4, "4"
    V = 5, "5"
    VI = 6, "6"