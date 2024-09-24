from django.urls import path
from .views import TankListApiView

app_name = "tanks"

urlpatterns = [
    path('list/', TankListApiView.as_view(), name="tank-list-api")
]