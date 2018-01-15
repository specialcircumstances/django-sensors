from .models import Location, Device, SensorType, Sensor, Reading
from rest_framework import serializers


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'desc')


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('name', 'uuid', 'location', 'ipaddress',
                  'authentication', 'authString')


class SensorTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorType
        fields = ('name', 'desc', 'displayType', 'displayUnits')


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('name', 'desc', 'device', 'sensortype',
                  'location', 'displayType', 'displayUnits')


class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reading
        fields = ('readingInt', 'readingFloat', 'sensor',
                  'sensor_timestamp', 'db_timestamp')
