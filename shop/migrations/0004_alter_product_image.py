# Generated by Django 3.2.9 on 2022-06-04 07:32

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20220501_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/default.png', upload_to='products', validators=[shop.models.validate_image]),
        ),
    ]
