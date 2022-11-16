fieldsets = (
    (None, {"fields": ("username", "password")}),
    (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
    (
        ("Permissions"),
        {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        },
    ),
    (("Important dates"), {"fields": ("last_login", "date_joined")}),
)

fieldsets[1] = ('Personal info', {'fields': ('first_name', 'last_name', 'email')})
print(fieldsets[1])