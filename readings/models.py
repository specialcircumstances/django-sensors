import uuid

from django.db import models
from django.urls import reverse

from datetime import date


# Create your models here.

class Location(models.Model):
    name = models.CharField("Name", db_index=True, max_length=64)
    desc = models.TextField("Notes", blank=True)

    def get_absolute_url(self):
        return reverse('readings:location', args={self.pk})

    def __str__(self):
        myresponse = "%s" % ( self.name )
        return myresponse

class Device(models.Model):
    name = models.CharField("Name", db_index=True, max_length=64)
    uuid = models.UUIDField("UUID", default=uuid.uuid4)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    ipaddress = models.GenericIPAddressField("IP Address")
    authentication = models.BooleanField("Authentication", blank=False,
        default=False)
    authString = models.CharField("Authentication String", max_length=64)

    def get_absolute_url(self):
        return reverse('readings:device', args={self.pk})

    def __str__(self):
        myresponse = "%s" % ( self.name )
        return myresponse

class SensorType(models.Model):
    name = models.CharField("Name", db_index=True, max_length=64)
    desc = models.TextField("Notes", blank=True)
    DISPLAYTYPES = {
        (0, 'Integer Number'),
        (1, 'Floating Point Number'),
        (2, 'Binary, Yes/No'),
    }
    displayType = models.IntegerField("Diplay Format",
        choices=DISPLAYTYPES, default=1)
    DISPLAYUNITS = {
        ('NUM', 'Generic: Number'),
        ('C', 'Temp: Celsius'),
        ('F', 'Temp: Farenhiet'),
        ('K', 'Temp: Kelvin'),
        ("%", 'Math: Percentage'),
        ('mW', 'Power: milliWatts'),
        ('W', 'Power: Watts'),
        ('kW', 'Power: KiloWatts'),
        ('MW', 'Power: MegaWatts'),
        ('mWh', 'Energy: milliWatt Hours'),
        ('Wh', 'Power: Watt Hours'),
        ('kWh', 'Power: KiloWatt Hours'),
        ('MWh', 'Power: MegaWatt Hours'),
        ('mV', 'Voltage: milliVolts'),
        ('V', 'Voltage: Volts'),
        ('mA', 'Current: milliAmps'),
        ('A', 'Current: Amps'),
        ('BYN', 'Binary: Yes/No'),
        ('BOO', 'Binary: On/Off'),
        ('BAI', 'Binary: Active/Inactive'),
        ('BPN', 'Binary: Present/Missing'),
    }
    displayUnits = models.CharField("Display Units", default='NUM',
        max_length=3, choices=DISPLAYUNITS)

    def get_absolute_url(self):
        return reverse('readings:sensortype', args={self.pk})

    def __str__(self):
        myresponse = "%s" % ( self.name )
        return myresponse

class Sensor(models.Model):
    name = models.CharField("Name", db_index=True, max_length=64)
    desc = models.TextField("Notes", blank=True)
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    sensortype = models.ForeignKey(SensorType, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    READINGTYPES = {
        (0, 'Integer Number'),
        (1, 'Floating Point Number'),
        (2, 'Binary, Yes/No'),
    }
    displayType = models.IntegerField("Readings Format",
        choices=READINGTYPES, default=1)
    READINGUNITS = {
        ('NUM', 'Generic: Number'),
        ('C', 'Temp: Celsius'),
        ('F', 'Temp: Farenhiet'),
        ('K', 'Temp: Kelvin'),
        ("%", 'Math: Percentage'),
        ('mW', 'Power: milliWatts'),
        ('W', 'Power: Watts'),
        ('kW', 'Power: KiloWatts'),
        ('MW', 'Power: MegaWatts'),
        ('mWh', 'Energy: milliWatt Hours'),
        ('Wh', 'Power: Watt Hours'),
        ('kWh', 'Power: KiloWatt Hours'),
        ('MWh', 'Power: MegaWatt Hours'),
        ('mV', 'Voltage: milliVolts'),
        ('V', 'Voltage: Volts'),
        ('mA', 'Current: milliAmps'),
        ('A', 'Current: Amps'),
        ('BYN', 'Binary: Yes/No'),
        ('BOO', 'Binary: On/Off'),
        ('BAI', 'Binary: Active/Inactive'),
        ('BPN', 'Binary: Present/Missing'),
    }
    displayUnits = models.CharField("Readings Units", default='NUM',
        max_length=3, choices=READINGUNITS)

    def get_absolute_url(self):
        return reverse('readings:sensor', args={self.pk})

    def __str__(self):
        myresponse = "%s" % ( self.name )
        return myresponse

class Reading(models.Model):
    readingInt = models.IntegerField("Integer Reading", blank=True, null=True)
    readingFloat = models.FloatField("Floating Point Reading", blank=True, null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    sensor_timestamp = models.DateField("Sensor Timestamp",
        blank=True, null=True)
    db_timestamp = models.DateTimeField("DB Timestamp", auto_now_add=True)

    def get_absolute_url(self):
        return reverse('readings:sensor', args={self.pk})

    def __str__(self):
        myresponse = "Int: %d  Float: %f " % ( self.readintInt,
            self.readingFloat )
        return myresponse
