from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


# Register your models here.

class UserAdmin_(UserAdmin):
    list_display = ['phone_number', 'last_name', 'first_name', 'image', 'description', 'is_staff']
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User


admin.site.register(User, UserAdmin_)
