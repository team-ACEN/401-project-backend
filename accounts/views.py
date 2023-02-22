from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CustomUser
# from .permissions import IsOwnerOrReadOnly
from .serializers import CustomUserSerializer


class CustomUserList(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

