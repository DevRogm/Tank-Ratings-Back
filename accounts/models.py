from django.contrib.auth.models import User
from django.db import models
from tanks.models import Tank


class WotPlayer(models.Model):
    user = models.OneToOneField(User, verbose_name="Użytkownik", on_delete=models.CASCADE, unique=True, related_name="wot_player")
    wot_account_id = models.IntegerField(verbose_name="ID konta w WOT", unique=True)
    nick = models.CharField(verbose_name="Nazwa gracza", max_length=64)
    console = models.CharField(verbose_name="Konsola", max_length=2)
    is_active = models.BooleanField(verbose_name="Czy konto jest aktywne?", default=False)
    tank_to_activate = models.IntegerField(verbose_name="Id czołgu do aktywacji konta", null=True, blank=True)
    time_to_activate = models.DateTimeField(verbose_name="Czas na aktywacje", null=True, blank=True)
    activated_at = models.DateTimeField(verbose_name="Data aktywacji", null=True, blank=True)
    available_tanks = models.ManyToManyField(Tank, verbose_name="Dostepne czołgi do oceniania", null=True, blank=True)

    class Meta:
        verbose_name = "Konto WoT użytkownika"
        verbose_name_plural = "Konto WoT użytkownika"

    def __str__(self):
        return f"{self.user.username} {self.nick}-{self.console}"