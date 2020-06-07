from django import forms
from registerapp.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
            model=UserProfileInfo
            fields=('first_name','last_name','email','phone','portfolio_site','profile_pic')
