from importlib.util import module_for_loader

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from tanks.models import Tank
from .constants import RatingRange
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    text = models.TextField(verbose_name="Treść komentarza", max_length=640)
    created_at = models.DateTimeField(verbose_name="Dodano", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Zmodyfikowano", null=True, blank=True, auto_now=True)

    class Meta:
        verbose_name = "Komentarz"
        verbose_name_plural = "Komentarze"

    def __str__(self):
        return f"{self.text[:20]}..."


class Rating(models.Model):
    author = models.ForeignKey(User, verbose_name="Autor oceny", on_delete=models.CASCADE,
                                  related_name="rating_author")
    comment = models.OneToOneField(Comment, verbose_name="Komentarz",on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name="rating_comment")
    tank = models.ForeignKey(Tank, verbose_name="Czołg", on_delete=models.CASCADE, related_name="rating_tank")
    gun_rating = models.PositiveSmallIntegerField(verbose_name="Ocena działa", choices=RatingRange, default=1, validators=[MinValueValidator(1), MaxValueValidator(6)])
    mobility_rating = models.PositiveSmallIntegerField(verbose_name="Ocena mobilności", choices=RatingRange, default=1, validators=[MinValueValidator(1), MaxValueValidator(6)])
    detection_rating = models.PositiveSmallIntegerField(verbose_name="Ocena wykrywania", choices=RatingRange, default=1, validators=[MinValueValidator(1), MaxValueValidator(6)])
    armor_rating = models.PositiveSmallIntegerField(verbose_name="Ocena pancerza", choices=RatingRange, default=1, validators=[MinValueValidator(1), MaxValueValidator(6)])
    cammo_rating = models.PositiveSmallIntegerField(verbose_name="Ocena kamuflarzu", choices=RatingRange, default=1, validators=[MinValueValidator(1), MaxValueValidator(6)])
    overall_rating = models.DecimalField(verbose_name="Ocena ogólna", max_digits=2, decimal_places=1)

    class Meta:
        unique_together = ('author', 'tank')
        verbose_name = "Ocena czołgu"
        verbose_name_plural = "Oceny czołgów"

    def __str__(self):
        return f"Czołg {self.tank} oceniony przez {self.author}"


class AvgRating(models.Model):
    tank = models.OneToOneField(Tank, verbose_name="Czołg", on_delete=models.CASCADE, related_name="avg_rating_tank")
    avg_gun_rating = models.DecimalField(verbose_name="Średnia ocena działa", max_digits=2, decimal_places=1)
    avg_mobility_rating = models.DecimalField(verbose_name="Średnia ocena mobilności", max_digits=2, decimal_places=1)
    avg_detection_rating = models.DecimalField(verbose_name="Średnia ocena wykrywania", max_digits=2, decimal_places=1)
    avg_armor_rating = models.DecimalField(verbose_name="Średnia ocena pancerza", max_digits=2, decimal_places=1)
    avg_cammo_rating = models.DecimalField(verbose_name="Średnia ocena kamuflarzu", max_digits=2, decimal_places=1)
    avg_overall_rating = models.DecimalField(verbose_name="Średnia ocena ogólna", max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = "Średnia ocena czołgu"
        verbose_name_plural = "Średnie oceny czołgów"

    def __str__(self):
        return f"Czołg {self.tank}"
