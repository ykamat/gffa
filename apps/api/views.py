
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from django.contrib.auth.models import User
from apps.webapp.models import Person, Planet
from .serializers import PersonSerializer, PlanetSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        queryset = Person.objects.all()
        name = self.request.query_params.get('name', None)
        home_world = self.request.query_params.get('home_world', None)
        if name:
            queryset = queryset.filter(name__contains=name)
        if home_world:
            queryset = queryset.filter(home_world__name__contains=home_world)
    
        return queryset.order_by('person_id')

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Planet.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__contains=name)
    
        return queryset.order_by('planet_id')
