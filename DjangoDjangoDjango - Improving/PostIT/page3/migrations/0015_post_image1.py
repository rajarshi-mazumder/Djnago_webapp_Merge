# Generated by Django 4.0.6 on 2022-08-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page3', '0014_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]