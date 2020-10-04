from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_models


# Register your models here.
class RoomInline(admin.StackedInline):
    model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                    "login_method",
                )
            },
        ),
    )

    inlines = [
        RoomInline,
    ]

    list_filter = UserAdmin.list_filter + (
        "superhost",
        "login_method",
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )
