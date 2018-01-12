from django.contrib import admin

# Register your models here.

from .models import Location, Device, SensorType, Sensor, Reading

admin.site.register(Location)
admin.site.register(Device)
admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(Reading)
