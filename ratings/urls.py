from django.urls import path
from ratings.views import RatingListApiView, RatingCreateApiView, RatingUpdateApiView, RatingDeleteApiView, \
    RatingDetailsApiView, CommentDeleteApiView

app_name = "ratings"

urlpatterns = [
    path('list/', RatingListApiView.as_view(), name="rating-list-api"),
    path('details/<int:pk>/', RatingDetailsApiView.as_view(), name="rating-list-api"),
    path('create/', RatingCreateApiView.as_view(), name="rating-create-api"),
    path('update/<int:pk>/', RatingUpdateApiView.as_view(), name="rating-update-api"),
    path('delete/<int:pk>/', RatingDeleteApiView.as_view(), name="rating-delete-api"),
    path('comment/delete/<int:pk>/', CommentDeleteApiView.as_view(), name="rating-comment-delete-api")
]
