from django import forms
from contactos.models import FormFactura
 
class FormFacturaForm(forms.ModelForm):
    class Meta:
        model = FormFactura
        fields = '__all__'