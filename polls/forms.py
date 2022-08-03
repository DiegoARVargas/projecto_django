from django import forms


class GoogleForm(forms.Form):
    input = forms.CharField(max_length=50)
    