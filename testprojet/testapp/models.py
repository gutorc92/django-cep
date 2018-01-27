from django.db import models
from cep.models import BRAddress
# Create your models here.
class TestModel(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    address = models.ForeignKey(BRAddress, on_delete=models.CASCADE)
