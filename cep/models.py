from django.utils.translation import gettext as _
from django.db import models

# Create your models here.

class BRAddress(models.Model):
    street = models.CharField(_('Street'), max_length=200, blank=True)
    district =models.CharField(_('District'), max_length=50, blank=True) 
    city = models.CharField(_('City'), max_length=100, blank=True)
    state = models.CharField(_('State'), max_length=30, blank=True)
    zip_code = models.PositiveIntegerField(_('ZipCode'))
