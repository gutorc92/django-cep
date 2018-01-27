from django import forms
from .models import TestModel
from cep.formfields import BRAddressField

class TestForm(forms.Form):

    name = forms.CharField(max_length=200, required=True)
    address = BRAddressField()

    
