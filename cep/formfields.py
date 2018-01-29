from django.core.exceptions import ValidationError
from django.forms.fields import Field
from django.utils.translation import ugettext_lazy as _
from cep.models import BRAddress
from cep.widgets import BRAddressWidget


class BRAddressField(Field):
    widget = BRAddressWidget
    is_hidden = False
    attrs = {}
    auto_id = 'id_br_address'

    default_error_messages = {
        'invalid': _('Enter a valid zip-code'),
    }

    def __init__(self, *, zip_code='', **kwargs):
        super().__init__(**kwargs)

    def to_python(self, value):
        b = BRAddress()
        b.street = value[0]
        b.district = value[1]
        b.city = value[2]
        b.state = value[3]
        b.zip_code = value[4] 
        print(value)
        return b

    
