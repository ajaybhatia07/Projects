# Generated by Django 3.2.4 on 2021-06-14 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_booking_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
    ]
