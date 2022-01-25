from django.urls import path
from .views import signup,login
from django6.views import *
from . import views

app_name='accounts'

urlpatterns=[
    path('login/',views.login,name='login'),
    path('signup/',views.signup, name='signup'),
    
]