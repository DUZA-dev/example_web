from django.db import models
from django.utils.html import mark_safe


class Organization(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)

    # В почтовом индексе иногда используются буквы, например в Канаде
    postcode = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def full_address(self):
        if self.postcode and self.address:
            return ", ".join([self.postcode, self.address])
        return self.postcode or self.address


class Event(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    date = models.DateTimeField()

    organizations = models.ManyToManyField(Organization, related_name="events")

    def __str__(self):
        return self.title

    @property
    def image_tag(self):
        try:
            return mark_safe('<img src="{}" width="100" height="100">'.format(self.image.url))
        except ValueError:
            return None
