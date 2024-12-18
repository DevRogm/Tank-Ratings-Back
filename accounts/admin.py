from django.contrib import admin
from .models import WotPlayer, ActivateAccount


@admin.register(WotPlayer)
class WotPlayerAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'wot_account_id', 'nick', 'console', 'is_active', 'activated_at')


@admin.register(ActivateAccount)
class ActivateAccountAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'wot_account_id', 'nick', 'console', 'can_activate', 'tank_id_to_activate', 'time_to_activate')
