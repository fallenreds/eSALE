# Generated by Django 4.0.3 on 2022-04-12 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
