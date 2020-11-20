from rest_framework import serializers

from django.contrib.auth.models import User
from apps.webapp.models import Film, Person, Planet, Species


class FilmSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Film
        fields = (
            'title',
            'episode_id',
            'opening_crawl',
            'director',
            'producer',
            'release_date',
            'species',
            # 'starships',
            # 'vehicles',
            'people',
            'planets',
            # 'url',
            # 'created',
            # 'edited'
        )


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


class SpeciesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Species

        fields = {
            'species_id',
            'name',
            # 'classification',
            # 'designation',
            # 'average_height',
            # 'skin_colors',
            # 'hair_colors',
            # 'eye_colors',
            'average_lifespan',
            'language',
            'home_world'
        }
