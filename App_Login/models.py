from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User ,related_name='user_profile',on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics')





class Contact(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=256)



    def __str__(self):
        return self.name + ' has messaged you!' 


    
    
