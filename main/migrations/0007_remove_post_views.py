# Generated by Django 4.0.3 on 2022-04-12 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_post_viewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
    ]