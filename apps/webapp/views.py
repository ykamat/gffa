from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from . forms import VehicleForm
from . models import Film, Person, Planet, Species, Starship, Vehicle, VehicleJurisdiction


class HomePageView(generic.TemplateView):
	template_name = 'webapp/home.html'


class AboutPageView(generic.TemplateView):
	template_name = 'webapp/about.html'


# def about(request):
#     # stripe_key = settings.STRIPE_KEYS['publishable']
#     # data = cache.get('resource_data')
#     # if not data:
#     #     data = get_resource_stats()
#     #     cache.set('resource_data', data, 10000)
#     # data['stripe_key'] = stripe_key

#     data = 'A long time ago in a galaxy far, far away.'
#     return render(request, "about.html", data)


class DocsPageView(generic.TemplateView):
	template_name = 'webapp/docs.html'


class RootPageView(generic.TemplateView):
	template_name = 'webapp/root.html'

class FilmPageView(generic.TemplateView):
	template_name = 'webapp/film_docs.html'


class PersonPageView(generic.TemplateView):
	template_name = 'webapp/person_docs.html'


class PlanetPageView(generic.TemplateView):
	template_name = 'webapp/planet_docs.html'


class SpeciesPageView(generic.TemplateView):
	template_name = 'webapp/species_docs.html'


class StarshipPageView(generic.TemplateView):
	template_name = 'webapp/starship_docs.html'


class VehiclePageView(generic.TemplateView):
	template_name = 'webapp/vehicle_docs.html'


class FilmDetailView(generic.DetailView):
	model = Film
	context_object_name = 'films'
	template_name = 'webapp/film_detail.html'

	def get_object(self):
		return super().get_object()

class FilmListView(generic.ListView):
	model = Film
	context_object_name = 'films'
	template_name = 'webapp/films.html'
	# paginate_by = 20

	# def dispatch(self, *args, **kwargs):
	# 	return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Film.objects.all()
		# return Person.objects.select_related('homeworld').order_by('name')


class PersonDetailView(generic.DetailView):
	model = Person
	context_object_name = 'persons'
	template_name = 'webapp/person_detail.html'

	def get_object(self):
		person = super().get_object()
		return person


class PersonListView(generic.ListView):
	model = Person
	context_object_name = 'persons'
	template_name = 'webapp/persons.html'
	# paginate_by = 20

	# def dispatch(self, *args, **kwargs):
	# 	return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Person.objects.all()
		# return Person.objects.select_related('homeworld').order_by('name')


class PlanetDetailView(generic.DetailView):
	model = Planet
	context_object_name = 'planets'
	template_name = 'webapp/planet_detail.html'

	def get_object(self):
		planet = super().get_object()
		return planet

class PlanetListView(generic.ListView):
	model = Planet
	context_object_name = 'planets'
	template_name = 'webapp/planets.html'
	# paginate_by = 20

	# def dispatch(self, *args, **kwargs):
	# 	return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Planet.objects.all()
		# return Person.objects.select_related('homeworld').order_by('name')


class SpeciesDetailView(generic.DetailView):
	model = Species
	context_object_name = 'species'
	template_name = 'webapp/species_detail.html'

	def get_object(self):
		species = super().get_object()
		return species


class SpeciesListView(generic.ListView):
	model = Species
	context_object_name = 'species'
	template_name = 'webapp/species.html'
	# paginate_by = 20

	# def dispatch(self, *args, **kwargs):
	# 	return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Species.objects.all()
		# return Species.objects.select_related('homeworld').order_by('name')


class StarshipDetailView(generic.DetailView):
	model = Starship
	context_object_name = 'starships'
	template_name = 'webapp/starship_detail.html'

	def get_object(self):
		starship = super().get_object()
		return starship


class StarshipListView(generic.ListView):
	model = Starship
	context_object_name = 'starships'
	template_name = 'webapp/starships.html'


	def get_queryset(self):
		return Starship.objects.all()
		# return Starship.objects.select_related('?').order_by('?')

@method_decorator(login_required, name='dispatch')
class VehicleCreateView(generic.View):
	model = Vehicle
	form_class = VehicleForm
	success_message = "Vehicle created successfully"
	template_name = 'webapp/vehicle_new.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = VehicleForm(request.POST)
		if form.is_valid():
			vehicle = form.save(commit=False)
			vehicle.save()
			VehicleJurisdiction.objects.create(vehicle=vehicle)
			return HttpResponseRedirect(vehicle.get_absolute_url())

		return render(request, 'webapp/vehicle_new.html', {'form': form})

	def get(self, request):
		form = VehicleForm()
		return render(request, 'webapp/vehicle_new.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class VehicleDeleteView(generic.DeleteView):
	model = Vehicle
	success_message = "Vehicle deleted successfully"
	success_url = reverse_lazy('vehicles')
	context_object_name = 'vehicles'
	template_name = 'webapp/vehicle_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Delete VehicleJurisdiction entries
		VehicleJurisdiction.objects \
			.filter(film_id=self.object.film_id) \
			.delete()

		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())

class VehicleDetailView(generic.DetailView):
	model = Vehicle
	context_object_name = 'vehicles'
	template_name = 'webapp/vehicle_detail.html'

	def get_object(self):
		return super().get_object()


class VehicleListView(generic.ListView):
	model = Vehicle
	context_object_name = 'vehicles'
	template_name = 'webapp/vehicles.html'

	def get_queryset(self):
		return Vehicle.objects.all()

@method_decorator(login_required, name='dispatch')
class VehicleUpdateView(generic.UpdateView):
	model = Vehicle
	form_class = VehicleForm
	context_object_name = 'vehicles'
	success_message = "Vehicle updated successfully"
	template_name = 'webapp/vehicle_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		vehicle = form.save(commit=False)
		vehicle.save()

		return HttpResponseRedirect(vehicle.get_absolute_url())