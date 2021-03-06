from rest_framework import serializers
from .models import *

#Serializers for different Models using ModelSerializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['user','first_name','last_name','email']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['sno','name','phone','email','content','timeStamp']
