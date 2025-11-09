from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('balance', 'is_kyc_verified', 'wallet_address')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
