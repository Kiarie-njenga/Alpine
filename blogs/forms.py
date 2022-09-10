





from .models import Blog, Blog_comment
from django.forms import ModelForm
from django import forms
import datetime
class BlogForm(ModelForm):
    
    class Meta:
        model=Blog
        fields=['category','title','thumbnail', 'files', 'main_content',]
        

class BlogCommentForm(forms.ModelForm):
    body=forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
        'rows':2,
        'style':'width:180px;border-radius:10px;',
        'placeholder':'comment..'
    }))
    
    class Meta:
        model=Blog_comment
        fields=['body',]