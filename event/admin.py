from django.contrib import admin

from event.models import Event, Organization
from core.models import User


class UserInline(admin.TabularInline):
    model = User.organizations.through
    extra = 2


@admin.register(Organization)
class Organization(admin.ModelAdmin):
    fields = (
        'title',
        'description',
        ('postcode', 'address'),
    )
    list_display = ['title', 'full_address']

    inlines = [UserInline, ]

    class Meta:
        model = Organization

    search_fields = ('title', 'description',)
    list_filter = ('postcode', )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'image_tag']
    readonly_fields = ['image_tag',]
    fields = (
        ('title', 'image_tag'),
        'description',
        'date',
        'organizations',
    )

    search_fields = ('title', 'description',)
    list_filter = ('date', )
