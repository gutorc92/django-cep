import json
from django.forms.widgets import MultiWidget, TextInput, NumberInput
from django.utils.safestring import mark_safe


class BRAddressWidget(MultiWidget):
    allow_multiple_selected = False
    template_name = "cep/field.html"
    #input_type = None

    def __init__(self,attrs=None, *args, **kwargs):
        widgets = (TextInput(attrs={'name':'street','id':'id_street_field'}), 
                   TextInput(attrs={'name':'district','id':'id_distric_field'}),
                   TextInput(attrs={'name':'city','id':'id_city_field'}), 
                   TextInput(attrs={'name':'state','id':'id_state_field'}), 
                   TextInput(attrs={'name':'zip_code',
                                     'id':'id_zip_code_field',
                                     'class': 'zip-field'}))

        super().__init__(widgets)

    def decompress(self, value):
        return [None, None]

    def id_for_label(self, id_):
        return id_

    def use_required_attribute(self, initial):
        return not self.is_hidden

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if self.is_localized:
            for widget in self.widgets:
                widget.is_localized = self.is_localized
        # value is a list of values, each corresponding to a widget
        # in self.widgets.
        if not isinstance(value, list):
            value = self.decompress(value)
       
        final_attrs = context['widget']['attrs']
        input_type = final_attrs.pop('type', None)
        id_ = final_attrs.get('id')
        subwidgets = []
        for i, widget in enumerate(self.widgets):
            if input_type is not None:
                widget.input_type = input_type
            if 'name' in widget.attrs:
                widget_name = widget.attrs['name']
            else:
                widget_name = '%s_%s' % (name, i)
            try:
                widget_value = value[i]
            except IndexError:
                widget_value = None
            if 'id' in widget.attrs:
                widget_attrs = final_attrs.copy()
                widget_attrs['id'] = widget.attrs['id']
            if 'class' in widget.attrs:
                widget_attrs['class'] = widget.attrs['class']
            subwidgets.append(widget.get_context(widget_name, widget_value, widget_attrs)['widget'])
        address = {'street' : 'id_street_field', 'district': 'id_district_field', 'city': 'id_city_field', 'state': 'id_state_field'}
        js_dict = json.dumps(address)
        output = u'var address = %s;' % js_dict
        context['widget']['subwidgets'] = subwidgets
        context['widget']['js_code'] = mark_safe(output)
        return context

    class Media:
        js = ('cep/js/cep.js',)
