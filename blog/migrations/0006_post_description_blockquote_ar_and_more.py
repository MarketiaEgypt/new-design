# Generated by Django 4.0.4 on 2022-05-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_description_blockquote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_blockquote_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description_blockquote_en',
            field=models.TextField(null=True),
        ),
    ]