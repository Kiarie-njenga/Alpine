# Generated by Django 3.2.9 on 2022-08-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20220514_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
