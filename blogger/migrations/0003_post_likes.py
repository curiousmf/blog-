# Generated by Django 4.2.3 on 2023-07-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
