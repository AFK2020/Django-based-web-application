from django.contrib import admin
from .models import CustomUser,Profile

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role')
    fieldsets = (
        ('Basic Information', {
            'fields': (('email','password') )
        }),
        ('Access Info',{
            'fields':(('is_active', 'is_staff', 'is_superuser'))
        }),
        ('Profile Info',{
            'fields':(('first_name', 'last_name', 'role','last_login'))
        }),
    )
    readonly_fields = ('last_login',)


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Profile)