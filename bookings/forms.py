from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['kunde', 'raum', 'check_in', 'check_out', 'anzahl_gaeste', 'status', 'notizen']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
            'notizen': forms.Textarea(attrs={'rows': 3}),
            'kunde': forms.Select(attrs={'class': 'customer-select2'}),
            'raum': forms.Select(attrs={'class': 'room-select2'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('kunde', css_class='form-group col-md-6 mb-3'),
                Column('raum', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('check_in', css_class='form-group col-md-4 mb-3'),
                Column('check_out', css_class='form-group col-md-4 mb-3'),
                Column('anzahl_gaeste', css_class='form-group col-md-4 mb-3'),
            ),
            Row(
                Column('status', css_class='form-group col-md-12 mb-3'),
            ),
            'notizen',
        )
