# Generated by Django 3.2.4 on 2021-06-13 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_number', models.IntegerField()),
                ('train_name', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('arrival', models.CharField(max_length=50)),
                ('departure', models.CharField(max_length=50)),
                ('ac_class', models.IntegerField(default=0)),
                ('ac_class_price', models.IntegerField(default=0)),
                ('sleeper_class', models.IntegerField(default=0)),
                ('sleeper_class_price', models.IntegerField(default=0)),
                ('second_sitting_class', models.IntegerField(default=0)),
                ('second_sitting_class_price', models.IntegerField(default=0)),
                ('first_class', models.IntegerField(default=0)),
                ('first_class_price', models.IntegerField(default=0)),
                ('executive_chair_class', models.IntegerField(default=0)),
                ('executive_chair_class_price', models.IntegerField(default=0)),
                ('running_days', multiselectfield.db.fields.MultiSelectField(choices=[('6', 'Sunday'), ('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday')], default=0, max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_name', models.CharField(max_length=100)),
                ('pass_age', models.IntegerField()),
                ('pass_gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('pass_select_class', models.CharField(choices=[('first', '1st Class'), ('second', '2nd Class'), ('sleeper', 'Sleeper Class'), ('sitting', '2nd Sitting')], max_length=10)),
                ('pass_pnr', models.CharField(max_length=50)),
                ('pass_train_number', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnr', models.IntegerField()),
                ('train_number', models.IntegerField()),
                ('train_name', models.CharField(default=0, max_length=100)),
                ('source', models.CharField(default=0, max_length=100)),
                ('destination', models.CharField(default=0, max_length=100)),
                ('number_of_seats', models.IntegerField()),
                ('booking_class', models.CharField(default=0, max_length=10)),
                ('booking_date', models.CharField(default=0, max_length=20)),
                ('status', models.BooleanField()),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]