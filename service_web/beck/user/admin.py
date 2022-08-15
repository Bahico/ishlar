from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.urls import reverse_lazy

from user.models import User


# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ("email", "username", "parent", "is_staff", "is_superuser", "is_active", "last_name",
#                   "phone", "referrals_count", "uuid", "tg_id")
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = User
#         fields = ('email', 'password')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['password'].help_text = ("<a href=\"%s\"><strong>Change Password</strong></a>"
#                                              ) % reverse_lazy('admin:auth_user_password_change',
#                                                               args=[self.instance.id])
#
#     def clean_password(self):
#         return self.initial["password"]
#
#
# class UserAdmin(admin.ModelAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#     list_display = ("id", "email", "username", "parent", "is_staff", "is_superuser",
#                     "is_active", "last_name", "phone", "referrals_count", "uuid", "tg_id"
#                     )
#     fieldsets = (
#         (None, {'fields': ("email", "username", "parent", "last_name", "phone",
#                            "referrals_count", "uuid", "tg_id", 'password')}),
#         ('Permissions', {'fields': ("is_staff", "is_active", 'is_superuser',)}),
#     )
#     add_fieldsets = (
#         (None, {'fields': ("email", "username", "parent", "last_name", "phone",
#                            'password1', 'password2',
#                            'is_active', 'is_staff')}),
#     )
#     list_filter = ("email",)
#     list_display_links = ('email',)
#     search_fields = ['email', 'id', 'last_name', ]


# admin.site.register(User)
