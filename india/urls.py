from india.views import *

from django.urls import path
app_name='app1'

urlpatterns=[
    path('virat/',virat,name='virat.html'),
]