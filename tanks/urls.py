from django.urls import path
from .views import TankListApiView, TankDetailsApiView

app_name = "tanks"

urlpatterns = [
    path('list/', TankListApiView.as_view(), name="tank-list-api"),
    path('details/<int:pk>/', TankDetailsApiView.as_view(), name="tank-details-api")
]