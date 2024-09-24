from django.urls import path
from ratings.views import RatingListApiView

app_name = "ratings"

urlpatterns = [
    path('list/', RatingListApiView.as_view(), name="rating-list-api")
]