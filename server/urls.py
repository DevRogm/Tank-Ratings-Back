"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from server import settings

schema_view = get_schema_view(
   openapi.Info(
      title="Tank-Ratings",
      default_version='v1',
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('tanks/', include("tanks.urls", namespace="tanks")),
    path('ratings/', include("ratings.urls", namespace="ratings")),
    path('news/', include("news.urls", namespace="news")),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path(r'__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns