from django.db import models
from .constants import Type, Tier, Nation


# Create your models here.
class Tank(models.Model):
    name = models.CharField(verbose_name="Nazwa czołgu", max_length=64)
    nation = models.CharField(verbose_name="Nacja", max_length=32, choices=Nation)
    tier = models.CharField(verbose_name="Poziom", max_length=8, choices=Tier)
    type = models.CharField(verbose_name="Typ czołgu", max_length=32, choices=Type)
    is_premium = models.BooleanField(verbose_name="Czołg premium", default=False)
    big_img = models.ImageField(verbose_name="Duże zdjęcie", upload_to='uploads/', null=True, blank=True)
    small_img = models.ImageField(verbose_name="Małe zdjęcie", upload_to='uploads/', null=True, blank=True)

    class Meta:
        verbose_name = "Czołg"
        verbose_name_plural = "Czołgi"

    def __str__(self):
        return f"Czołg: {self.name}, {self.nation}"
