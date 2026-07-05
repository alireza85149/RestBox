from django import forms
from .models import Villa

class VillaForm(forms.ModelForm):
    class Meta:
        model = Villa
        fields = ['title', 'address', 'capacity', 'price_per_night']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Villa Title'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Villa Address'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max capacity'}),
            'price_per_night': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'price'}),
        }
        labels = {
            'title': 'Villa Title',
            'address': 'Villa Address',
            'capacity': 'Max capacity',
            'price_per_night': 'price',
        }