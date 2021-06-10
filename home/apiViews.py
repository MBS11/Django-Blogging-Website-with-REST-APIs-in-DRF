from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class ProfileModelViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class ContactModelViewSet(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]