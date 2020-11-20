from django.contrib import admin

from . models import Person, Planet, Species, Film, Starships, Vehicles


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """Film administration."""

    fields = [
        'film_id',
        'title',
        'episode_id',
        'opening_crawl',
        'director',
        'producer',
        'release_date',
        'characters',
        'planets',
        # 'starships',
        # 'vehicles',
        'species'
    ]

    list_display = [
        'film_id',
        'title',
        'episode_id',
        'opening_crawl',
        'director',
        'producer',
        'release_date',
        'get_characters',
        'get_planets',
        # 'get_starships',
        # 'get_vehicles',
        'get_species'
    ]

    ordering = ['title']

    list_filter = ['title']


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

    ordering = ['name']

    list_filter = ['name']


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

    ordering = ['name']

    list_filter = ['name']


@admin.register(Starships)
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

    ordering = ['name']

    list_filter = ['name']


@admin.register(Vehicles)
class VehiclesAdmin(admin.ModelAdmin):
    """Vehicles administration."""

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

    ordering = ['name']

    list_filter = ['name']
