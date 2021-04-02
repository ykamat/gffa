from rest_framework import serializers
from django.contrib.auth.models import User
from apps.webapp.models import Film, Person, Planet, Vehicle, Species, Starship, FilmCharacter, FilmPlanet


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
            # 'species',
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


class StarshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Starship
        fields = (
            "name",
            "starship_class",
            "manufacturer",
            "cost_in_credits",
            "length",
            "crew",
            "passengers",
            "max_atmosphering_speed",
            "hyperdrive_rating",
            "MGLT",
            "cargo_capacity",
            "consumables",
            # "pilots"
        )


class FilmCharacterSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.ReadOnlyField(source='film.id')
    film_id = serializers.ReadOnlyField(source='film.film_id')
    character_id = serializers.ReadOnlyField(source='character.person_id')

    class Meta:
        model = FilmCharacter

        fields = {
            # 'film_person_id',
            'film_id',
            'character_id',
        }

class FilmPlanetSerializer(serializers.HyperlinkedModelSerializer):
    film_id = serializers.ReadOnlyField(source='film.film_id')
    planet_id = serializers.ReadOnlyField(source='planet.planet_id')

    class Meta:
        model = FilmCharacter

        fields = {
            'film_id',
            'planet_id',
        }
