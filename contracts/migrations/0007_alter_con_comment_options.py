# Generated by Django 3.2.9 on 2022-06-28 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_auto_20220627_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='con_comment',
            options={'ordering': ['-created_on']},
        ),
    ]
