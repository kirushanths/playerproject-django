from django.contrib import admin
from .models import DZUser

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .forms import DZUserModelForm, DZUserChangeForm

class DZUserAdmin(UserAdmin):
    add_form = DZUserModelForm
    form = DZUserChangeForm
    
    list_display = ('email', 'is_staff',)
    list_filter = ('is_staff', 'is_superuser',
                         'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields':
                                ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active',
                                'is_staff',
                                'is_superuser',
                                'groups',
                                'user_permissions')}),
        ('Important dates', {'fields': ('last_login','last_activity')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',
                        'password1', 'password2')}
        ),
    )
 
admin.site.register(DZUser)