from django.contrib.auth.models import User
from django.db import models
from tanks.models import Tank


class WotPlayer(models.Model):
    user = models.OneToOneField(User, verbose_name="Użytkownik", on_delete=models.CASCADE, unique=True,
                                related_name="wot_player")
    wot_account_id = models.IntegerField(verbose_name="ID konta w WOT", unique=True)
    nick = models.CharField(verbose_name="Nazwa gracza", max_length=64)
    console = models.CharField(verbose_name="Konsola", max_length=2)
    is_active = models.BooleanField(verbose_name="Czy konto jest aktywne?", default=False)
    activated_at = models.DateTimeField(verbose_name="Data aktywacji", auto_now=True)
    available_tanks = models.ManyToManyField(Tank, verbose_name="Dostepne czołgi do oceniania", blank=True)

    class Meta:
        verbose_name = "Konto WoT użytkownika"
        verbose_name_plural = "Konto WoT użytkownika"

    def __str__(self):
        return f"{self.user.username} {self.nick}-{self.console}"


class ActivateAccount(models.Model):
    user = models.OneToOneField(User, verbose_name="Użytkownik", on_delete=models.CASCADE, unique=True,
                                related_name="activate_account")
    wot_account_id = models.IntegerField(verbose_name="ID konta w WOT", unique=True)
    nick = models.CharField(verbose_name="Nazwa gracza", max_length=64)
    console = models.CharField(verbose_name="Konsola", max_length=2)
    tank_id_to_activate = models.IntegerField(verbose_name="Id czołgu do aktywacji konta", null=True, blank=True)
    tank_name_to_activate = models.CharField(verbose_name="Nazwa czołgu do aktywacji konta", null=True, blank=True)
    tank_tier_to_activate = models.CharField(verbose_name="Tier czołgu do aktywacji konta", null=True, blank=True)
    time_to_activate = models.DateTimeField(verbose_name="Czas na aktywacje", null=True, blank=True)
    can_activate = models.BooleanField(verbose_name="Czy konto można aktywować?", default=False)

    class Meta:
        verbose_name = "Aktywowanie kont"
        verbose_name_plural = "Aktywowanie kont"

    def __str__(self):
        return f"{self.user.username} {self.nick}-{self.console}"
