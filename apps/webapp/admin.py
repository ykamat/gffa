from django.contrib import admin
from . models import Person, Planet, Species, Film, Starship, Vehicle, FilmPerson, FilmPlanet

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """Film administration."""

    fields = [
        'title',
        'episode_id',
        'opening_crawl',
        'director',
        'producer',
        'release_date',
    ]
    list_display = [
        'title',
        'episode_id',
        'opening_crawl',
        'director',
        'producer',
        'release_date',
        'film_characters',
        'film_planets',
        # 'film_species',
        # 'film_starships',
        # 'film_vehicles'
    ]
    list_filter = ['title']
    filter_horizontal = [
        'characters',
        'planets',
        # 'species',
        # 'starships',
        # 'vehicles'
    ]
    ordering = ['title']


@admin.register(FilmPerson)
class FilmPersonAdmin(admin.ModelAdmin):
    """FilmPerson administration."""

    fields = ['film', 'person']
    list_display = ['film', 'person']
    list_filter = ['film']
    ordering = ['film', 'person']


@admin.register(FilmPlanet)
class FilmPlanetAdmin(admin.ModelAdmin):
    """FilmPlanet administration."""

    fields = ['film', 'planet']
    list_display = ['film', 'planet']
    list_filter = ['film']
    ordering = ['film', 'planet']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Person administration."""

    fields = [
        'name',
        'species',
        'birth_year',
        'gender',
        'height',
        'mass',
        'eye_color',
        'hair_color',
        'skin_color',
        'home_world'
    ]
    list_display = [
        'name',
        'species',
        'birth_year',
        'gender',
        'height',
        'mass',
        'eye_color',
        'hair_color',
        'skin_color',
        'home_world'
    ]
    list_filter = ['name']
    ordering = ['name']


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    """Planet administration."""

    fields = [
        'name',
        'rotation_period',
        'orbital_period',
        'diameter',
        'climate',
        'gravity',
        'terrain',
        'surface_water',
        'population'
    ]

    list_display = [
        'name',
        'rotation_period',
        'orbital_period',
        'diameter',
        'climate',
        'gravity',
        'terrain',
        'surface_water',
        'population'
    ]

    ordering = ['name']

    list_filter = ['name']


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    """Species administration."""

    fields = [
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
    ]
    list_display = [
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
    ]
    list_filter = ['name']
    ordering = ['name']


@admin.register(Starship)
class StarshipAdmin(admin.ModelAdmin):
    """Starship administration."""

    fields = [
        'name',
        'starship_class',
        'manufacturer',
        'cost_in_credits',
        'length',
        'crew',
        'passengers',
        'max_atmosphering_speed',
        'hyperdrive_rating',
        'MGLT',
        'cargo_capacity',
        'consumables',
        'pilots'
    ]
    list_display = [
        'starship_class',
        'manufacturer',
        'cost_in_credits',
        'length',
        'crew',
        'passengers',
        'max_atmosphering_speed',
        'hyperdrive_rating',
        'MGLT',
        'cargo_capacity',
        'consumables',
        'pilots'
    ]
    list_filter = ['name']
    ordering = ['name']


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """Vehicle administration."""

    fields = [
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
    ]
    list_display = [
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
    ]
    list_filter = ['name']
    ordering = ['name']
