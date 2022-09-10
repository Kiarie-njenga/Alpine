









from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.





class BuyerRequest(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    body=models.TextField('Requesting')
    pic=models.ImageField(upload_to='stories/', default='stories/default.png', blank=True)
    class Meta:
        ordering=('-date',)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('buyer_request_detail', args=[str(self.id)])

class Comment(models.Model):
    comment=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    buyer_request=models.ForeignKey(BuyerRequest,  on_delete=models.CASCADE)
    active=models.BooleanField(default=False)
    class Meta:
        ordering=['-created_on']
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('buyer_request_detail')
    