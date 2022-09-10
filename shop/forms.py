






from django import forms
from .models import Product

from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    category=forms.Select()
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'placeholder':'e.g corn, beans..', 'class':'form-control'}))
    image=forms.FileField(label='Picture',widget=forms.FileInput(attrs={'class':'form-control'}))
    description=forms.CharField(label='Description',widget=forms.Textarea(attrs={'rows':3,'placeholder':'e.g varities, color..'}))
    price=forms.DecimalField(label='Price',widget=forms.NumberInput(attrs={'placeholder':'e.g $13'}))
    available=forms.BooleanField(label='Available', required=False)
    class Meta:
        model=Product
        fields=['category','name','image','description','units', 'price','available']
    