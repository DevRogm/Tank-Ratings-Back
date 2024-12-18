from django.urls import path
from .views import RegistrationView, ActiveAccountCreateView, ActiveAccountDeleteView, ActiveAccountRetrieveView

app_name = 'accounts'


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),

    #activate account
    path('activate/create/', ActiveAccountCreateView.as_view(), name='activate_account_create'),
    path('activate/get/<int:pk>/', ActiveAccountRetrieveView.as_view(), name='activate_account_get'),
    path('activate/delete/<int:pk>/', ActiveAccountDeleteView.as_view(), name='activate_account_delete'),

]
