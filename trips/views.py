from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from trips.models import Trip
from trips.serializers import TripSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def trip_list(request):
    if request.method == 'GET':
        trips = Trip.objects.all()
        
        start = request.GET.get('start', None)
        if start is not None:
            trips = trips.filter(start__icontains=start)
        
        trips_serializer = TripSerializer(trips, many=True)
        return JsonResponse(trips_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        trip_data = JSONParser().parse(request)
        trip_serializer = TripSerializer(data=trip_data)
        if trip_serializer.is_valid():
            trip_serializer.save()
            return JsonResponse(trip_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(trip_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Trip.objects.all().delete()
        return JsonResponse({'message': '{} Viaje  fué eliminiado satisfactoriamente!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def trip_total_viajes(request):
    if request.method == 'GET':
        trips = Trip.objects.all()
        count=Trip.objects.count()

        start = request.GET.get('start', None)
        if start is not None:
            trips = trips.filter(start__icontains=start)
        
        trips_serializer = TripSerializer(trips, many=True)
        return JsonResponse({'message': 'Existen {} Viajes!'.format(count)}, status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
def trip_total_viajes_ciudad(request, pk):
    try: 
        #trip = Trip.objects.get(pk=pk) 
        count = Trip.objects.all().filter(cityname='Bogotá').count()
        
        
    except Trip.DoesNotExist: 
        return JsonResponse({'message': 'La ciudad no existe'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        trip_serializer = TripSerializer(trip) 
        return JsonResponse({'message': 'Existen {} Viajes!'.format(count)}, status=status.HTTP_204_NO_CONTENT)
 
    elif request.method == 'PUT': 
        trip_data = JSONParser().parse(request) 
        trip_serializer = TripSerializer(trip, data=trip_data) 
        if trip_serializer.is_valid(): 
            trip_serializer.save() 
            return JsonResponse(trip_serializer.data) 
        return JsonResponse(trip_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        trip.delete() 
        return JsonResponse({'message': 'trip borrado exitosamente!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def trip_detail(request, pk):
    try: 
        trip = Trip.objects.get(pk=pk) 
    except Trip.DoesNotExist: 
        return JsonResponse({'message': 'trip no  existe'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        trip_serializer = TripSerializer(trip) 
        return JsonResponse(trip_serializer.data) 
 
    elif request.method == 'PUT': 
        trip_data = JSONParser().parse(request) 
        trip_serializer = TripSerializer(trip, data=trip_data) 
        if trip_serializer.is_valid(): 
            trip_serializer.save() 
            return JsonResponse(trip_serializer.data) 
        return JsonResponse(trip_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        trip.delete() 
        return JsonResponse({'message': 'trip fue eliminado satisfactoriamente!'}, status=status.HTTP_204_NO_CONTENT)

    