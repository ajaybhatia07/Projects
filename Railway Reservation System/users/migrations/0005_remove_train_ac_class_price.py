# Generated by Django 3.2.4 on 2021-06-18 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210619_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='ac_class_price',
        ),
    ]