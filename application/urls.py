from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
     path('',views.home,name="home"),
     path('login/',views.user_login,name="login"),
     path('signup/',views.signup,name="signup"),
     path('homepage/<str:user>/',views.homepage,name="homepage"),
     path('deposit/',views.deposit,name="deposit"),
     path('withdrawal/',views.withdrawal,name="withdrawal"),
     path('checkbalance/',views.checkbalance,name="balance"),
     path('logout/',views.logout,name="logout")
]
