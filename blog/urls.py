from django.contrib import admin
from django.urls import path, include
from . import views
from . import apiViews
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('Category-api', apiViews.CategoryModelViewSet,basename='category')
router.register('Post-api', apiViews.PostModelViewSet,basename='post')

urlpatterns = [
     path('postComment', views.postComment, name="postComment"),
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path('api/',include(router.urls)),
]
