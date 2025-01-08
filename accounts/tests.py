import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.constants import URL_REGISTER, URL_LOGIN, URL_REFRESH

"""
TEST CASES:

=== Registration ===
- test_user_registration_with_correct_data                      V
- test_user_registration_with_password_mismatch                 V
- test_user_registration_with_too_short_password                V
- test_user_registration_with_too_common_password               V
- test_user_registration_with_password_similar_to_username      V
- test_user_registration_with_duplicate_username                V
- test_user_registration_without_username                       V

=== Login ===
- test_login_with_valid_credentials                             V
- test_login_with_invalid_credentials                           V            
- test_refresh_token                                            V
- test_refresh_token_with_invalid_token                         V

=== Activate === need to use mock
- test_check_if_wot_player_exist_with_valid_credentials
- test_check_if_wot_player_exist_with_invalid_credentials
- test_draw_the_tank
- test_create_activate_account_first_time
- test_create_activate_account_duplicate
- test_can_activate_account
"""


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_user_registration_with_correct_data(api_client):
    payload = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "StrongPassword123!",
        "password2": "StrongPassword123!"
    }
    expected_response = {'username': payload['username'], 'email': payload['email']}
    response = api_client.post(URL_REGISTER, payload)
    user = User.objects.filter(username="testuser").first()
    assert response.status_code == status.HTTP_201_CREATED
    assert expected_response == response.data
    assert user.email == payload['email']
    assert user.check_password(payload['password'])
    assert user.check_password(payload['password2'])


@pytest.mark.django_db
def test_user_registration_with_password_mismatch(api_client):
    payload = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "StrongPassword123!",
        "password2": "WrongPassword123!"
    }
    response = api_client.post(URL_REGISTER, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "password" in response.data
    assert response.data["password"] == ["Hasła nie są takie same"]


@pytest.mark.django_db
def test_user_registration_with_too_short_password(api_client):
    payload = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "haslo!",
        "password2": "haslo!"
    }
    response = api_client.post(URL_REGISTER, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "password" in response.data
    assert response.data["password"] == ["To hasło jest za krótkie. Musi zawierać co najmniej 8 znaków."]


@pytest.mark.django_db
def test_user_registration_with_too_common_password(api_client):
    payload = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password",
        "password2": "password"
    }
    response = api_client.post(URL_REGISTER, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "password" in response.data
    assert response.data["password"] == ["To hasło jest zbyt powszechne."]


@pytest.mark.django_db
def test_user_registration_with_password_similar_to_username(api_client):
    payload = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testuser",
        "password2": "testuser"
    }
    response = api_client.post(URL_REGISTER, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "password" in response.data
    assert response.data["password"] == ["Hasło jest zbyt podobne do nazwy użytkownika"]


@pytest.mark.django_db
def test_user_registration_with_duplicate_username(api_client):
    payload_1 = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "StrongPassword123!",
        "password2": "StrongPassword123!"
    }

    payload_2 = {
        "username": "testuser",
        "email": "testuser2@example.com",
        "password": "AnotherStrongPassword456!",
        "password2": "AnotherStrongPassword456!"
    }

    response_1 = api_client.post(URL_REGISTER, payload_1)
    response_2 = api_client.post(URL_REGISTER, payload_2)

    assert response_1.status_code == status.HTTP_201_CREATED
    assert response_2.status_code == status.HTTP_400_BAD_REQUEST
    assert "username" in response_2.data
    assert response_2.data["username"] == ["Użytkownik o tej nazwie już istnieje."]


@pytest.mark.django_db
def test_user_registration_without_username(api_client):
    payload = {
        "email": "testuser@example.com",
        "password": "testuser",
        "password2": "testuser"
    }
    response = api_client.post(URL_REGISTER, payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "username" in response.data
    assert response.data["username"] == ["To pole jest wymagane."]


@pytest.fixture
def create_test_user():
    user = User.objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="StrongPassword123!"
    )
    return user


@pytest.mark.django_db
def test_login_with_valid_credentials(api_client, create_test_user):
    payload = {
        "username": "testuser",
        "password": "StrongPassword123!"
    }
    response = api_client.post(URL_LOGIN, payload)
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_login_with_invalid_credentials(api_client, create_test_user):
    payload = {
        "username": "testuser",
        "password": "WrongPassword458!"
    }
    response = api_client.post(URL_LOGIN, payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert "access" not in response.data
    assert "refresh" not in response.data


@pytest.mark.django_db
def test_refresh_token(api_client, create_test_user):
    refresh = RefreshToken.for_user(create_test_user)
    payload = {
        "refresh": str(refresh)
    }
    response = api_client.post(URL_REFRESH, payload)
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data


@pytest.mark.django_db
def test_refresh_token_with_invalid_token(api_client):
    payload = {
        "refresh": "invalid_token"
    }
    response = api_client.post(URL_REFRESH, payload)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert "access" not in response.data