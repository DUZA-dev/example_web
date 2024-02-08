from django.db import models
from django.utils.html import mark_safe


class Organization(models.Model):
    """ Модель организаций """
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=512, blank=True)

    # В почтовом индексе иногда используются буквы, например в Канаде
    postcode = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title

    @property
    def full_address(self) -> str:
        """ Склеиваем адрес организации """
        if self.postcode and self.address:
            return ", ".join([self.postcode, self.address])
        return self.postcode or self.address


class Event(models.Model):
    """ События устраиваемые организациями """
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True)
    date = models.DateTimeField()

    organizations = models.ManyToManyField(Organization, related_name="events")

    def __str__(self):
        return self.title

    @property
    def image_tag(self):
        """ Вывод в админку картинки """
        try:
            return mark_safe('<img src="{}" width="100" height="100">'.format(self.image.url))
        except ValueError:
            return None
