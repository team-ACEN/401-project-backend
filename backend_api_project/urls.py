"""backend_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include ,path
from backend_app import views
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('streaming_services/genres/', views.get_genres, name='streaming_services_genres'),
    path('streaming_services/search/', views.search, name='streaming_services_search'),
    path('streaming_services/services/', views.get_services, name='streaming_services_services'),
    path('streaming_services/popular/', views.get_popular_based_on_service, name='streaming_services_popular'),
    path("api/users/", include("accounts.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/",
        MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    )
]
