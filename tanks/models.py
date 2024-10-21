from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .constants import Type, Tier, Nation


# Create your models here.
class Tank(models.Model):
    tank_id = models.IntegerField(verbose_name="ID czołgu", validators=[MinValueValidator(1)], unique=True)
    name = models.CharField(verbose_name="Nazwa czołgu", max_length=64)
    short_name = models.CharField(verbose_name="Skrócona Nazwa czołgu", max_length=64)
    nation = models.CharField(verbose_name="Nacja", max_length=32)
    tier = models.IntegerField(verbose_name="Poziom", validators=[MinValueValidator(1), MaxValueValidator(10)])
    era = models.CharField(verbose_name="Era", max_length=8, choices=Tier, null=True, blank=True)
    type = models.CharField(verbose_name="Typ czołgu", max_length=32)
    is_premium = models.BooleanField(verbose_name="Czołg premium", default=False)
    url_img = models.URLField(verbose_name="Link do obrazka", null=True, blank=True)
    big_img = models.ImageField(verbose_name="Duże zdjęcie", upload_to='uploads/', null=True, blank=True)
    small_img = models.ImageField(verbose_name="Małe zdjęcie", upload_to='uploads/', null=True, blank=True)

    class Meta:
        verbose_name = "Czołg"
        verbose_name_plural = "Czołgi"

    def __str__(self):
        return f"Czołg: {self.name}, {self.nation}"
