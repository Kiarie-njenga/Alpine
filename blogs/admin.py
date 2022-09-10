from django.contrib import admin
from .models import Blog, Blog_comment, Category
# Register your models here.





admin.site.register(Blog)
admin.site.register(Blog_comment)
admin.site.register(Category)