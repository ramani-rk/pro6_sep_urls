from nz.views import *
from django.urls import path

app_name ='Worldcup Semi'

urlpatterns = [
    path('kane/',kane,name='kane'),
    path('conway/',conway,name='conway'),
]