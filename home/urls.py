from django.contrib import admin
from django.urls import path,include
from home import views
from . import apiViews
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('UserProfile-api', apiViews.ProfileModelViewSet,basename='profile')
router.register('ContactUs-api', apiViews.ContactModelViewSet,basename='contact')

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('search', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('api/',include(router.urls)),
]
 