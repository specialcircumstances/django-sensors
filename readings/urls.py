from django.urls import path

from . import views
from .models import Location, Device, SensorType, Sensor, Reading

urlpatterns = [
    path('', views.index, name='index'),
    path('location/<int:item_id>/', views.location, name='location'),
    path('device/<int:item_id>/', views.device, name='device'),
    path('sensortype<int:item_id>/', views.sensortype, name='sensortype'),
    path('sensor/<int:item_id>/', views.sensor, name='sensor'),
    path('reading/<int:item_id>/', views.reading, name='reading'),
]
