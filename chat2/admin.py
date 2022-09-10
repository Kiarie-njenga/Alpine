







from django.contrib import admin
from .models import  Messages, Friends
from profiles.models import Profile
# Register your models here.

admin.site.register(Messages)
admin.site.register(Friends)