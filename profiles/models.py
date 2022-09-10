





from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

class ProfileType(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User, primary_key=True, related_name='profile', on_delete=models.CASCADE)
    name=models.CharField(max_length=30, blank=True, null=True)
    bio=models.TextField(blank=True, default='')
    date_of_birth=models.DateField(null=True, blank=True)
    phone=models.CharField(max_length=15, unique=True, null=True)
    location=models.CharField(max_length=40, blank=True, null=True)
    what_describes_you=models.ForeignKey(ProfileType, on_delete=models.CASCADE, null=True)
    pic=models.ImageField(upload_to='uploads/profiles/', default='uploads/profiles/default.png', blank=True)


    def get_absolute_url(self):
        return reverse('profiles:profile', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

