import datetime

import pytz
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError
from rest_framework import serializers

from accounts.constants import TANK_TIER_TO_ACTIVATE_ACCOUNT
from accounts.models import ActivateAccount
from accounts.services import AccountService
from tanks.models import Tank

from wot_client.services import WotClient


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError({"password": "Hasła nie są takie same"})
        if data.get('username') in data.get('password'):
            raise serializers.ValidationError({"password": "Hasło jest zbyt podobne do nazwy użytkownika"})
        return data

    @staticmethod
    def validate_password(value):
        try:
            validate_password(value)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value


    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                username = validated_data.get('username'),
                email = validated_data.get('email'),
                password = validated_data.get('password')
            )
            return user
        except Exception as error:
            raise serializers.ValidationError({"details": "Nie udało się utworzyć konta użytkownika"})


class ActivateAccountSerializer(serializers.ModelSerializer):
    nick = serializers.CharField(write_only=True)
    console = serializers.CharField(write_only=True)

    time_to_activate = serializers.DateTimeField(read_only=True)
    tank_name_to_activate = serializers.CharField(read_only=True)
    tank_tier_to_activate = serializers.CharField(read_only=True)

    class Meta:
        model = ActivateAccount
        fields = ('time_to_activate', 'console', 'nick', 'tank_name_to_activate', 'tank_tier_to_activate')

    def create(self, validated_data):
        # Check if wot player exists
        try:
            nick = validated_data.get('nick')
            console = validated_data.get('console')
            wot_client = WotClient()
            wot_player = wot_client.get_player_id_by_nick_and_console(nick, console)
            if not wot_player:
                raise serializers.ValidationError(
                    {"details": f"Nie znaleziono konta użytkownika z podanym nickiem ({nick}) dla wybranej konsoli ({console})"})
        except Exception as error:
            print("ActivateAccountSerializer:", error)
            raise serializers.ValidationError({"details": "Nie udało się zweryfikować użytkownika"})
        # If wot player exists draw the tank
        try:
            account_service = AccountService()
            drawn_tank = account_service.draw_tank_to_active_account(tier=TANK_TIER_TO_ACTIVATE_ACCOUNT)
        except Exception as error:
            print("ActivateAccountSerializer:", error)
            raise serializers.ValidationError({"details": "Nie udało się wylosować czołgu"})
        # After draw the tank create ActivateAccount for this player in db
        try:
            tz = pytz.timezone(settings.TIME_ZONE)
            time_now = datetime.datetime.now(tz=tz)
            time_for_activation = time_now + datetime.timedelta(minutes=30)
            player_activate_account = ActivateAccount(user=self.context.get('user'),
                                                      wot_account_id=wot_player[0]['account_id'],
                                                      nick=nick,
                                                      console=console,
                                                      tank_id_to_activate=drawn_tank.tank_id,
                                                      tank_name_to_activate=drawn_tank.name,
                                                      tank_tier_to_activate=drawn_tank.tier,
                                                      time_to_activate=time_for_activation
                                                      )
            player_activate_account.save()
        except IntegrityError as error:
            print("ActivateAccountSerializer:", error)
            raise serializers.ValidationError({"details": "Konto jest w trakcie aktywacji"})
        except Exception as error:
            print("ActivateAccountSerializer:", error)
            raise serializers.ValidationError({"details": "Nie udało się rozpocząć procedury aktywacji konta"})
        return player_activate_account
