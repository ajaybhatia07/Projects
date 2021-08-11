from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.fields import related
from multiselectfield import MultiSelectField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to ='profile_pics')

    def __str__(self):
       return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height >  300 or img.width > 300:
            output_size = (300,300) 
            img.thumbnail(output_size)
            img.save(self.image.path)


class Train(models.Model):
    DAYS = (
        ('6','Sunday'),
        ('0','Monday'),
        ('1','Tuesday'),
        ('2','Wednesday'),
        ('3','Thursday'),
        ('4','Friday'),
        ('5','Saturday')
    )
    train_number=models.IntegerField()
    train_name=models.CharField(max_length=50)
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    arrival=models.CharField(max_length=50)
    departure=models.CharField(max_length=50)
    ac_class=models.IntegerField(default = 0) 
    sleeper_class=models.IntegerField(default = 0)
    second_sitting_class=models.IntegerField(default = 0)
    first_class=models.IntegerField(default = 0)
    executive_chair_class=models.IntegerField(default = 0)
    running_days = MultiSelectField(choices = DAYS, default = 0)

    def __str__(self):
        return self.train_name

class Booking(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE, default = 0)
    date = models.CharField(max_length = 100, default = 0)
    pnr = models.IntegerField()
    train_number = models.IntegerField()
    train_name = models.CharField(max_length = 100, default = 0)
    source = models.CharField(max_length = 100, default = 0)
    destination = models.CharField(max_length = 100, default = 0) 
    number_of_seats = models.IntegerField()
    booking_class = models.CharField(max_length = 10, default = 0)
    status = models.BooleanField()

    def __str__(self):
        return f'PNR Number - {self.pnr}' 