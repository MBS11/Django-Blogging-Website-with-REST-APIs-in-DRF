from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class BCmntModelViewSet(viewsets.ModelViewSet):
    queryset=BlogComment.objects.all()
    serializer_class=BCmntSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class PostModelViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    filter_backends=[SearchFilter]
    search_fields=['category','title','slug']