from nz.views import *

from django.urls import path
app_name='app1'

urlpatterns=[
    path('msd/',msd,name='msd.html'),
]