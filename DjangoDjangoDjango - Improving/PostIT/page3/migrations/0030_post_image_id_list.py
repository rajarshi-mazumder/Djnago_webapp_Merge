# Generated by Django 4.0.6 on 2022-08-22 11:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page3', '0029_remove_post_image1_imagefiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_id_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None),
        ),
    ]
