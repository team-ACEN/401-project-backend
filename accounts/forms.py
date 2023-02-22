from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ("username", "email", "genres", "services")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "genres", "services")
