from django import forms

from coderdjango.familiares.models import Familiar

class FormularioFamiliar(forms.ModelForm):
    class Meta:
        model = Familiar
        fields = '__all__'
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}
