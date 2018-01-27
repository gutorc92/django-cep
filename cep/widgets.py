import json
from django.forms.widgets import Widget
from django.utils.safestring import mark_safe


class BRAddressWidget(Widget):
    allow_multiple_selected = True
    template_name = "cep/field.html"
    input_type = None

    def __init__(self,attrs=None, *args, **kwargs):
        super().__init__(attrs)


    def id_for_label(self, id_):
        return id_

    def use_required_attribute(self, initial):
        return not self.is_hidden
    
    class Media:
        js = ('cep/js/cep.js',)
