import random

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WeatherData, Cities
from .producer import publish
from .serializers import WeatherDataSerializer, CitiesSerializer


class WeatherDataViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/weatherdata
        weather_data = WeatherData.objects.all()
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/weatherdata
        serializer = WeatherDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('weather_data_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/weatherdata/<str:id>
        weather_data = WeatherData.objects.get(id=pk)
        serializer = WeatherDataSerializer(weather_data)
        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/weatherdata/<str:id>
        weather_data = WeatherData.objects.get(id=pk)
        serializer = WeatherDataSerializer(instance=weather_data, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('weather_data_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/weatherdata/<str:id>
        weather_data = WeatherData.objects.get(id=pk)
        weather_data.delete()
        publish('weather_data_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CitiesViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/cities
        cities = Cities.objects.all()
        serializer = CitiesSerializer(cities, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/cities
        serializer = CitiesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/cities/<str:id>
        cities = Cities.objects.get(id=pk)
        serializer = CitiesSerializer(cities)
        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/cities/<str:id>
        cities = Cities.objects.get(id=pk)
        serializer = CitiesSerializer(instance=cities, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/cities/<str:id>
        cities = Cities.objects.get(id=pk)
        cities.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CitiesAPIView(APIView):
    def get(self, _):
        cities = Cities.objects.all()
        city = random.choice(cities)
        return Response({
            'name': city.name
        })
