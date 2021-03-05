from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
         return "Message from " + self.name + ' - ' + self.email


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,blank='true',null='true')
    first_name= models.CharField(max_length=100,blank='true',null='true')
    last_name= models.CharField(max_length=100,blank='true',null='true')
    email= models.CharField(max_length=100,blank='true',null='true')

    def __str__(self):
         return str(self.user)
    

def create_Profile(sender, instance, created , **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile created")

post_save.connect(create_Profile, sender=User)