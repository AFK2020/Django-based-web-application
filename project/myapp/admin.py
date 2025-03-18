from django.contrib import admin
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ("email",)
    fieldsets = (
        ("Basic Information", {"fields": (("email", "password"))}),
        ("Access Info", {"fields": (("is_active", "is_staff", "is_superuser"))}),
        ("Profile Info", {"fields": (("first_name", "last_name", "last_login"))}),
    )
    readonly_fields = ("last_login", "password")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("role", "ip_address")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
