from django.db import models
from django.utils.translation import gettext_lazy as _

TYPES = [
    (1, 'Sedan'),
    (2, 'Truck'),
    (3, 'SUV'),
]


class Manufacturer(models.Model):
    name = models.CharField(_('name'), max_length=100,)
    country_code = models.CharField(_('country code'), max_length=2,)
    created = models.DateField(_('created'),)


class Car(models.Model):
    name = models.CharField(_('name'), max_length=100,)
    color = models.CharField(_('color'), max_length=30,)
    description = models.TextField(_('description'),)
    type = models.IntegerField(_('type'), choices=TYPES,)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name=_('manufacturer'),)

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

    def __str__(self):
        return self.name

    def get_auction_title(self):
        return '{} - {}'.format(self.name, self.color)
