from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class News(models.Model):
    author = models.ForeignKey(User, verbose_name="Autor nowinki", max_length=256, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Tytuł nowinki", max_length=32, unique=True)
    text = models.TextField(verbose_name="Treść nowinki")
    created_at = models.DateTimeField(verbose_name="Utworzono", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Zmodyfikowano", auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = "Nowinki"
        verbose_name_plural = "Nowinki"
