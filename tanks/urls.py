from django.urls import path
from .views import TankListApiView, TankDetailsApiView, TankTop10ApiView, TankAvailableApiView

app_name = "tanks"

urlpatterns = [
    path('list/', TankListApiView.as_view(), name="tank-list-api"),
    path('top10/', TankTop10ApiView.as_view(), name="tank-top10-api"),
    path('available/', TankAvailableApiView.as_view(), name="tank-available-api"),
    path('details/<int:pk>/', TankDetailsApiView.as_view(), name="tank-details-api"),
]