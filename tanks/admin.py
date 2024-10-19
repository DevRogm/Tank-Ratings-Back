from django.contrib import admin
from .models import Tank


@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'nation', 'type', 'tier', 'is_premium', 'era')
