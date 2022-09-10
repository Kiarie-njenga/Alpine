from django.db import models







# Create your models here.
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse




class Contract(models.Model):
    title=models.CharField(max_length=255)
    start_of_contract=models.DateTimeField()
    end_of_contract=models.DateTimeField()
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_active=models.BooleanField(default=True)
    payment_cost_details=models.CharField(max_length=255)
    project_specific_details=RichTextField()
    legal_disclaimers=models.FileField()
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('contract:contract_detail', args=[str(self.id)])

class Con_comment(models.Model):
    body=models.TextField(default='', blank=True)
    created_on=models.DateTimeField(auto_now_add=True, null=True)
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    contract=models.ForeignKey(Contract, null=True, on_delete=models.CASCADE)
    
    class Meta:
        ordering=['-created_on']
    def __str__(self):
        return self.body
    def get_absolute_url(self):
        return reverse('contract:contract_detail')