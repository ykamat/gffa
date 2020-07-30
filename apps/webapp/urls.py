from __future__ import unicode_literals

# from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.urls import path
# from rest_framework import routers
# from resources import views as resource_views
from . import views


# admin.autodiscover()
# router = routers.DefaultRouter()

# router.register(r"people", resource_views.PeopleViewSet)
# router.register(r"planets", resource_views.PlanetViewSet)
# router.register(r"films", resource_views.FilmViewSet)
# router.register(r"species", resource_views.SpeciesViewSet)
# router.register(r"vehicles", resource_views.VehicleViewSet)
# router.register(r"starships", resource_views.StarshipViewSet)


# urlpatterns = patterns("",
#     url(r"^admin/", include(admin.site.urls)),
#     url(r"^$", "swapi.views.index"),
#     url(r"^documentation$", "swapi.views.documentation"),
#     url(r"^about$", "swapi.views.about"),
#     url(r"^stats$", "swapi.views.stats"),
#     url(r"^stripe/donation", "swapi.views.stripe_donation"),
#     url(r"^api/people/schema$", "resources.schemas.people"),
#     url(r"^api/planets/schema$", "resources.schemas.planets"),
#     url(r"^api/films/schema$", "resources.schemas.films"),
#     url(r"^api/species/schema$", "resources.schemas.species"),
#     url(r"^api/vehicles/schema$", "resources.schemas.vehicles"),
#     url(r"^api/starships/schema$", "resources.schemas.starships"),
#     url(r"^api/", include(router.urls)),
# )

urlpatterns = [
    # path(r"^admin/", include(admin.site.urls)),
    # path('', swapi_views.index, name='index'),
    path('docs/', views.DocsPageView.as_view(), name='docs'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    # path(r"^stats$", "swapi.views.stats"),
    # path(r"^stripe/donation", "swapi.views.stripe_donation"),
    # path(r"^api/people/schema$", "resources.schemas.people"),
    # path(r"^api/planets/schema$", "resources.schemas.planets"),
    # path(r"^api/films/schema$", "resources.schemas.films"),
    # path(r"^api/species/schema$", "resources.schemas.species"),
    # path(r"^api/vehicles/schema$", "resources.schemas.vehicles"),
    # path(r"^api/starships/schema$", "resources.schemas.starships"),
    # path(r"^api/", include(router.urls)),
]
