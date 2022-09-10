from django.db import models
from django.urls import reverse





from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

def validate_image(image):
        width=image.width
        height=image.height
        if height<width:
            raise ValidationError('Image is too small')

class Units(models.Model):
    name=models.CharField(max_length=20, default='KG')
    def __str__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200 )
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=200 )
    likes=models.ManyToManyField(User, blank=True, related_name="likers")
    dislikes=models.ManyToManyField(User, blank=True, related_name="dislikes")
    image = models.ImageField(upload_to='products', validators=[validate_image], default='products/default.png')
    description = models.TextField(blank=True)
    units=models.ForeignKey(Units,null=True,  on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        

    def total_likes(self):
        return self.likes.count()
    def total_dislikes(self):
        return self.dislikes.count()
    def __str__(self):
        return self.name

    

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[str(self.id)])