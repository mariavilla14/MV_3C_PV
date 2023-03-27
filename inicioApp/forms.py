from django import forms

from inicioApp.models import aficionado


class formularioafi(forms.ModelForm):
    class Meta:
        model=aficionado
        fields= '__all__'
        widgets={'fecha_nacimiento':forms.DateInput(attrs={'type':'date'})}