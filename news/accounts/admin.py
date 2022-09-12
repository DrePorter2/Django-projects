from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomAccountCreationForm, CustomAccountChangeForm
from .models import CustomAccount


class CustomAccountAdmin(UserAdmin):
    add_form = CustomAccountCreationForm
    form = CustomAccountChangeForm
    model = CustomAccount
    list_display = ['email', 'username', 'age', 'is_staff', ]

admin.site.register(CustomAccount, CustomAccountAdmin)
