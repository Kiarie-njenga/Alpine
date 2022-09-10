







from django import forms
from .models import BuyerRequest, Comment


class CommentForm(forms.ModelForm):
    comment=forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
        'rows':2,
        'placeholder':'comment..'
    }))
    
    class Meta:
        model=Comment
        fields=['comment',]



class BuyerRequestForm(forms.ModelForm):
    body=forms.CharField(
        
        widget=forms.Textarea(attrs={
        'rows':3,
        'placeholder':'place a request..'
    }))
    
    class Meta:
        model=BuyerRequest
        fields=['title','body','pic',]
