from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['anrede', 'vorname', 'nachname', 'email', 'telefon', 
                  'strasse', 'plz', 'stadt', 'land', 'notizen']
        widgets = {
            'notizen': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('anrede', css_class='form-group col-md-4 mb-3'),
                Column('vorname', css_class='form-group col-md-4 mb-3'),
                Column('nachname', css_class='form-group col-md-4 mb-3'),
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-3'),
                Column('telefon', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('strasse', css_class='form-group col-md-12 mb-3'),
            ),
            Row(
                Column('plz', css_class='form-group col-md-3 mb-3'),
                Column('stadt', css_class='form-group col-md-5 mb-3'),
                Column('land', css_class='form-group col-md-4 mb-3'),
            ),
            'notizen',
        )
