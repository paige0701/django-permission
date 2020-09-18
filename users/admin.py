from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django_reverse_admin import ReverseModelAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser, CustomGroup


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'groups')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'first_name', 'last_name', 'groups')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class CustomGroupAdmin(ReverseModelAdmin):
    model = CustomGroup
    inline_type = 'tabular'
    inline_reverse = [
                      ('group', {'fields': ['name']}), 'description'
                      ]


admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

