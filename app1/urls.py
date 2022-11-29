from django.urls import path
from app1.views import *
app_name='aa'
urlpatterns=[
    path('hai/',hai,name='hai'),
    path('jalsa/', jalsa, name='jalsa'),
]