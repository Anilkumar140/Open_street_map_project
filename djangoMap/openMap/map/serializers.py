from map.models import *
from rest_framework import serializers


class MyCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = my_cities
        fields = '__all__'
 
class MyLatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_latlong
        fields = ['id','lattitude','longitude', 'city']