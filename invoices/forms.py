from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['buchung', 'rechnungsdatum', 'faelligkeitsdatum', 'status', 'mwst_satz', 'notizen']
        widgets = {
            'rechnungsdatum': forms.DateInput(attrs={'type': 'date'}),
            'faelligkeitsdatum': forms.DateInput(attrs={'type': 'date'}),
            'notizen': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('buchung', css_class='form-group col-md-12 mb-3'),
            ),
            Row(
                Column('rechnungsdatum', css_class='form-group col-md-6 mb-3'),
                Column('faelligkeitsdatum', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('status', css_class='form-group col-md-6 mb-3'),
                Column('mwst_satz', css_class='form-group col-md-6 mb-3'),
            ),
            'notizen',
        )
