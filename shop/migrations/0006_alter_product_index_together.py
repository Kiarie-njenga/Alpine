# Generated by Django 3.2.9 on 2022-06-08 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_likes'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='product',
            index_together=set(),
        ),
    ]
