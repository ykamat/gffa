from rest_framework import serializers

from django.contrib.auth.models import User
from apps.webapp.models import Person, Planet

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Person
        fields = (
            'name',
            'birth_year',
            'eye_color',
            'gender',
            'hair_color',
            'height',
            'mass',
            'skin_color',
            'home_world',
            # 'films',
            'species',
            # 'starships',
            # 'vehicles',
            'url',
            # 'created',           
            # 'edited',
            )

class PlanetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Planet
        fields = (
            'name',
            'diameter',
            'rotation_period',
            'orbital_period',
            # 'gravity',
            'population',
            'climate',
            'terrain',
            # 'surface_water',
            # 'residents',
            # 'films',
            # 'url',
            # 'created',
            # 'edited',
        )