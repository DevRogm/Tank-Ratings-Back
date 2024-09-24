from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _

class RatingRange(IntegerChoices):
    I = 1, _("1")
    II = 2, _("2")
    III = 3, _("3")
    IV = 4, _("4")
    V = 5, _("5")
    VI = 6, _("6")