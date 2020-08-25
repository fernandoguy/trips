from rest_framework import serializers 
from trips.models import Trip
 
 
class TripSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Trip
        fields = ('id',
        'startdatedate',
        'startpickup_address',
        'startpickup_locationtype',
        'startpickup_locationcoordinates0',
        'startpickup_locationcoordinates1',
        'enddate',
        'endpickup_address',
        'endpickup_locationtype',
        'endpickup_locationcoordinates0',
        'endpickup_locationcoordinates1',
        'countryname',
        'cityname',
        'passengerfirst_name',
        'passengerlast_name',
        'driverfirst_name',
        'driverlast_name',
        'carplate',
        'status',
        'check_code',
        'createdAtdate',
        'updatedAtdate',
        'price',
        'driver_locationtype',
        'driver_locationcoordinates0',
        'driver_locationcoordinates1',
        'driver_location',
        )
        