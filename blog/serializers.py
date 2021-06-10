from rest_framework import serializers
from .models import *

#Serializers for different Models using ModelSerializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['sno','title','timeStamp','author_id','slug','thumbnail','material','category','views']

class BCmntSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogComment
        fields=['sno','comment','user','post','parent','timestamp']