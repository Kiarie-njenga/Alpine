from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Blog(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    title=models.CharField(max_length=200)
    thumbnail=models.ImageField(upload_to='uploads/files/', default='stories/default.png', blank=True)
    files=models.FileField(upload_to='uploads/files/', null=True, blank=True)
    main_content=RichTextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

class Blog_comment(models.Model):
    body=models.TextField(default='', blank=True)
    created_on=models.DateTimeField(auto_now_add=True, null=True)
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering=['-created_on']
    
    def __str__(self):
        return self.body
    def get_absolute_url(self):
        return reverse('blog_detail')
   