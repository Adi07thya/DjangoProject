from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(blank=True,max_length=30)
    last_name=models.CharField(blank=True,max_length=30)
    email=models.EmailField(blank=True,max_length=250)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

def __str__(self):
    return self.user.username
