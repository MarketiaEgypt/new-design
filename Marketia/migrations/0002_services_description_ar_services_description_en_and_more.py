# Generated by Django 4.0.4 on 2022-04-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='description_ar',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='description_en',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='name_ar',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='name_en',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
