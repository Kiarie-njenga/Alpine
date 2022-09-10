





from .models import Contract, Con_comment
from django.forms import ModelForm
from django import forms
import datetime
class ContractForm(ModelForm):
    
    class Meta:
        model=Contract
        fields=['title', 'start_of_contract', 'end_of_contract','is_active','payment_cost_details', 'project_specific_details' , 'legal_disclaimers']
        widgets={
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title',
            }),
            'start_of_contract':forms.DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':datetime.datetime.now(),
            }),
            'end_of_contract':forms.DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':datetime.datetime.now()+datetime.timedelta(days=270),
            }),
            'payment_cost_details':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'$, shs',
                'rows':4
            }),
            'project_specific_details':forms.Textarea(attrs={
                'class':'form-control',
                
            }),
            'legal_disclaimers':forms.FileInput(attrs={
                'class':'form-control',
                
            }),
            
        }

class CommentForm(forms.ModelForm):
    body=forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
        'rows':2,
        'style':'width:180px;border-radius:10px;',
        'placeholder':'request..'
    }))
    
    class Meta:
        model=Con_comment
        fields=['body',]