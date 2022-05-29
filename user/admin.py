from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Liked posts',
            {
                'fields': (
                    'liked_posts',
                )
            }
        )
    )


admin.site.register(User, CustomUserAdmin)
