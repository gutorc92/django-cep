from django import forms
from .models import TestModel
from cep.formfields import BRAddressField

class TestForm(forms.Form):

    name = forms.CharField(max_length=200, required=True)
    address = BRAddressField()


    def save(self):
        t = TestModel()    
        cleaned_data = super(TestForm, self).clean()
        t.name = cleaned_data.get('name')
        t.address = cleaned_data.get('address')
        t.address.save()
        print(t.address.pk)
        t.address_id = t.address.pk
        t.save()
        return t
