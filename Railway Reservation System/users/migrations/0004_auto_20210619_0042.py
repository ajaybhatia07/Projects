# Generated by Django 3.2.4 on 2021-06-18 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_booking_booking_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='executive_chair_class_price',
        ),
        migrations.RemoveField(
            model_name='train',
            name='first_class_price',
        ),
        migrations.RemoveField(
            model_name='train',
            name='second_sitting_class_price',
        ),
        migrations.RemoveField(
            model_name='train',
            name='sleeper_class_price',
        ),
    ]
