# Generated by Django 4.1.13 on 2024-04-11 07:49

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_userprofile_username_userprofile_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='User',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]