# Generated by Django 3.2.9 on 2022-06-09 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyers', '0002_alter_buyerrequest_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
