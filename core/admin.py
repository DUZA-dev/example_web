from django.contrib import admin

from core.models import User


@admin.register(User)
class Organization(admin.ModelAdmin):
    fields = (
        ('email', 'telephone'),
        'password',
        ('is_staff', 'is_superuser'),
        'organizations',
    )
    list_display = ['email', 'telephone', 'is_staff', 'is_superuser',]
    search_fields = ('email', 'telephone', )
    list_filter = ('is_staff', 'is_superuser', )

    class Meta:
        model = User
