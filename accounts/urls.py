from django.urls import path
from .views import CustomUserList, CustomUserDetail

urlpatterns = [
    path("", CustomUserList.as_view(), name="custom_user_list"),
    path("<int:pk>/", CustomUserDetail.as_view(), name="custom_user_detail"),
]
