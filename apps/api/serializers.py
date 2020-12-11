from rest_framework import serializers
from django.contrib.auth.models import User
from apps.webapp.models import Film, Person, Planet, Vehicle, Species, FilmPerson


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
            'characters',
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


class VehicleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Vehicle
        fields = (
            'name',
            'vehicle_class',
            'manufacturer',
            'length',
            'cost_in_credits',
            'crew',
            'passengers',
            'max_atmosphering_speed',
            'cargo_capacity',
            'consumables'
        )
class SpeciesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Species

        fields = {
            'species_id',
            'name',
            'classification',
            'designation',
            'average_height',
            'skin_colors',
            'hair_colors',
            'eye_colors',
            'average_lifespan',
            'language',
            'home_world'
        }

class FilmPersonSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='film.id')

    class Meta:
        model = FilmPerson

        fields = {
            # 'film_person_id',
            'film',
            'person',
        }
