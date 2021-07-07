from django.urls import path

from .views import WeatherDataViewSet, CitiesViewSet, WeatherAPIView

urlpatterns = [
    path('weatherdata', WeatherDataViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('weatherdata/<str:pk>', WeatherDataViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('cities', CitiesViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('cities/<str:pk>', CitiesViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('city/<str:name>', WeatherAPIView.as_view())
]