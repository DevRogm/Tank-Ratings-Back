from django.urls import path

from news.views import NewsListApiView, NewsDetailsApiView, NewsCreateApiView, NewsDeleteApiView, NewsUpdateApiView

app_name = 'news'

urlpatterns = [
    path('list/', NewsListApiView.as_view(), name="news-list-api"),
    path('details/<int:pk>/', NewsDetailsApiView.as_view(), name="news-list-api"),
    path('create/', NewsCreateApiView.as_view(), name="news-create-api"),
    path('update/<int:pk>/', NewsUpdateApiView.as_view(), name="news-update-api"),
    path('delete/<int:pk>/', NewsDeleteApiView.as_view(), name="news-delete-api"),
]