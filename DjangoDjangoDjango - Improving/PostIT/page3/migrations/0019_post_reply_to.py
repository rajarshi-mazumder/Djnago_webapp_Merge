# Generated by Django 4.0.6 on 2022-08-20 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page3', '0018_profile_discord_link_profile_profile_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reply_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='page3.post'),
        ),
    ]
