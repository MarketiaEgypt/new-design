# Generated by Django 4.0.4 on 2022-07-14 09:28

import Marketia.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketia', '0002_remove_services_icon_services_description_ar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientLogo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to=Marketia.models.path_and_rename)),
            ],
        ),
    ]