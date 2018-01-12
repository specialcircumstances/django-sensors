from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
from .models import Location, Device, SensorType, Sensor, Reading

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
