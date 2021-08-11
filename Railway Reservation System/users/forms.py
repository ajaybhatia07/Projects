from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms.widgets import NumberInput
import datetime

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class TicketBookingForm(forms.ModelForm):
    CLASSES = (
        ('ac_class','AC'),
        ('sleeper_class','SL'),
        ('second_sitting_class','2S'),
        ('first_class','FC'),
        ('executive_chair_class','EC')
    )
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    select_class = forms.ChoiceField(choices = CLASSES)

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date
        
    class Meta:
        model = Train

        fields = ['source','destination']

class PassengerDetailsForm(forms.Form):
    GENDER = [
        ('male','Male'),
        ('female','Female')
    ]

    name = forms.CharField(max_length=100)
    age = forms.DecimalField()
    gender = forms.ChoiceField(choices = GENDER)
    total_passengers = forms.IntegerField()
    class Meta:
        fields = ['name','age','gender','total_passengers']