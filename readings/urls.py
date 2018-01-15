from django.urls import path, re_path, include
from rest_framework import routers

from . import views
from .models import Location, Device, SensorType, Sensor, Reading

router = routers.DefaultRouter()
router.register(r'locations', views.LocationAPIViewSet)
router.register(r'devices', views.DeviceAPIViewSet)
router.register(r'sensortypes', views.SensorTypeAPIViewSet)
router.register(r'sensors', views.SensorAPIViewSet)
router.register(r'readings', views.ReadingAPIViewSet)


urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
    path('', views.index, name='index'),
    path('location/<int:item_id>/', views.location, name='location'),
    path('device/<int:item_id>/', views.device, name='device'),
    path('sensortype<int:item_id>/', views.sensortype, name='sensortype'),
    path('sensor/<int:item_id>/', views.sensor, name='sensor'),
    path('reading/<int:item_id>/', views.reading, name='reading'),
]
