from django import forms
from .models import Deudor


class GoogleForm(forms.Form):
    input = forms.CharField(max_length=50)

class DeudorForm(forms.ModelForm):
    class Meta:
        model = Deudor
        fields = '__all__'

#1. Abstraccion de los imputs de los formularios.
#2. puedes definir validaciones customizadas  para cada imput (clean_<atributo>)
class ConvertForm(forms.Form):
    origen = forms.CharField(max_length=3)
    destiny = forms.CharField(max_length=3)

    def clean_origen(self):
        # codigo de validacion
        valid_codes = [
            'ARS',
            'COP',
            'BRL',
        ]
        dato_dela_view = self.cleaned_data['origen']
        if dato_dela_view not in valid_codes:
            raise forms.ValidationError(f'Moneda {dato_dela_view} invalid!!')
        return dato_dela_view
