# Generated by Django 4.0.6 on 2022-08-22 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page3', '0028_delete_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image1',
        ),
        migrations.CreateModel(
            name='ImageFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page3.post')),
            ],
        ),
    ]