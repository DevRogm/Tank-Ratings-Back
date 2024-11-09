from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


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