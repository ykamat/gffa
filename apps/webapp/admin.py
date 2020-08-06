from django.contrib import admin
from . models import Person


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