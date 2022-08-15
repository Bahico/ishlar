from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from user.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('phone_number', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name', 'description')
