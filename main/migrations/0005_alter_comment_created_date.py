# Generated by Django 4.0.3 on 2022-04-11 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата'),
        ),
    ]