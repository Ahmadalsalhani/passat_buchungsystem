from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff']
    list_filter = ['role', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    readonly_fields = ['created_at', 'updated_at', 'last_login', 'date_joined']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Zusätzliche Informationen', {'fields': ('role', 'created_at', 'updated_at')}),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Zusätzliche Informationen', {'fields': ('role',)}),
    )
