# Generated by Django 3.0.3 on 2020-03-16 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20200315_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='item',
            name='start_time',
        ),
    ]