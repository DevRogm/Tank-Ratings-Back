from django.contrib import admin
from .models import WotPlayer


@admin.register(WotPlayer)
class WotPlayerAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'wot_account_id', 'nick', 'console', 'is_active', 'activated_at', 'tank_to_activate', 'time_to_activate')
