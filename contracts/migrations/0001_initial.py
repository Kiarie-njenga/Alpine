# Generated by Django 3.2.9 on 2022-05-20 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start_of_contract', models.DateTimeField()),
                ('end_of_contract', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('payment_cost_details', models.CharField(max_length=255)),
                ('project_specific_details', models.TextField()),
                ('legal_disclaimers', models.FileField(upload_to='')),
            ],
        ),
    ]
