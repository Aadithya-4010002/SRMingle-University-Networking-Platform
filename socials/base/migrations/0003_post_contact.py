# Generated by Django 4.1.13 on 2024-03-29 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contact',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]