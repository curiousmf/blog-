# Generated by Django 4.2.3 on 2023-07-14 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
