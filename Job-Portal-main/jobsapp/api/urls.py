

from django.urls import path,include 
from rest_framework import routers
from jobsapp.api.views import HydJobsCRUDCBV


routers=routers.DefaultRouter()
routers.register('hydjobsinfo',HydJobsCRUDCBV)




urlpatterns = [
    path('', include(routers.urls)),
    
    
]
