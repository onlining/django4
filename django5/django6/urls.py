from django.urls import path
from .views import Home
from django6.views import *


app_name='django6'

urlpatterns=[
    path('', Home.as_view(), name="django5"),
    
]