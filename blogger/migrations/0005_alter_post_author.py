# Generated by Django 4.2.1 on 2023-10-15 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0004_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=30),
        ),
    ]
