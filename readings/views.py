from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets


# Create your views here.
from .models import Location, Device, SensorType, Sensor, Reading
from .serializers import LocationSerializer, DeviceSerializer
from .serializers import SensorTypeSerializer, SensorSerializer
from .serializers import ReadingSerializer


# REST API views


class LocationAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DeviceAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class SensorTypeAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer


class SensorAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ReadingAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer


def index(request):
    template = loader.get_template('readings/index.html')
    context = {
        'message': "Readings Template. With bootstrap4"
    }
    return HttpResponse(template.render(context, request))

def location(request, item_id):
    response = "You're looking at the results of location %s."
    return HttpResponse(response % item_id)

def device(request, item_id):
    response = "You're looking at the results of device %s."
    return HttpResponse(response % item_id)

def sensortype(request, item_id):
    response = "You're looking at the results of sensortype %s."
    return HttpResponse(response % item_id)

def sensor(request, item_id):
    response = "You're looking at the results of sensor %s."
    return HttpResponse(response % item_id)

def reading(request, item_id):
    response = "You're looking at the results of reading %s."
    return HttpResponse(response % item_id)
