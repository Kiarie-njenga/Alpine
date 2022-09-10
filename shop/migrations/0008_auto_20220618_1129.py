# Generated by Django 3.2.9 on 2022-06-18 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0007_auto_20220611_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='units',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.units'),
        ),
    ]
