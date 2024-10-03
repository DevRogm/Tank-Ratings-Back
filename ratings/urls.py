from django.urls import path
from ratings.views import RatingListApiView, RatingCreateApiView

app_name = "ratings"

urlpatterns = [
    path('list/', RatingListApiView.as_view(), name="rating-list-api"),
    path('create/', RatingCreateApiView.as_view(), name="rating-create-api")
]