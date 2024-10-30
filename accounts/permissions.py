from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Tylko właściciel tej oceny może ją edytować lub usunąć.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class IsWotPlayer(permissions.BasePermission):
    message = 'Tylko gracz WoT może oceniać czołgi, aktywuj konto zgodnie z instrukcją'

    def has_permission(self, request, view):
        try:
            wot_player = request.user.wot_player
        except AttributeError:
            return False
        return wot_player.is_active