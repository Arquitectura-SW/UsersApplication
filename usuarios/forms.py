from django import forms 
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'name',
            'lastName',
            'documuent',
            'birthdate',
            'email',
            'country',
            'city',
        ]
        
        labels = {
            'name':'name',
            'lastName':'lastName',
            'document': 'document',
            'birthdate': 'birthdate',
            'email': 'email',
            'country': 'country',
            'city': 'city',
        }