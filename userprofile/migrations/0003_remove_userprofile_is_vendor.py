# Generated by Django 4.2.7 on 2023-12-18 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_is_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_vendor',
        ),
    ]
