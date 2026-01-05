from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['raumnummer', 'raumname', 'raumtyp', 'kapazitaet', 
                  'preis_pro_nacht', 'beschreibung', 'aktiv']
        widgets = {
            'beschreibung': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('raumnummer', css_class='form-group col-md-4 mb-3'),
                Column('raumname', css_class='form-group col-md-8 mb-3'),
            ),
            Row(
                Column('raumtyp', css_class='form-group col-md-6 mb-3'),
                Column('kapazitaet', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('preis_pro_nacht', css_class='form-group col-md-6 mb-3'),
                Column('aktiv', css_class='form-group col-md-6 mb-3'),
            ),
            'beschreibung',
        )
