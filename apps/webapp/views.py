from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from . forms import FilmForm, VehicleForm
from . models import Film, FilmCharacter, FilmPlanet, Person, Planet, Species, Starship, Vehicle, VehiclePassenger



class HomePageView(generic.TemplateView):
	template_name = 'webapp/home.html'


class AboutPageView(generic.TemplateView):
	template_name = 'webapp/about.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['Films'] = Film.objects.all().count()
		context['Persons'] = Person.objects.all().count()
		context['Planets'] = Planet.objects.all().count()
		context['Species'] = Species.objects.all().count()
		context['Starships'] = Starship.objects.all().count()
		context['Vehicles'] = Vehicle.objects.all().count()

		return context


class ContributerPageView(generic.TemplateView):
	template_name = 'webapp/contributers.html'


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


@method_decorator(login_required, name='dispatch')
class FilmCreateView(generic.View):
	model = Film
	form_class = FilmForm
	success_message = "Film created successfully"
	template_name = 'webapp/film_new.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = FilmForm(request.POST)
		if form.is_valid():
			film = form.save(commit=False)
			film.save()

			for character in form.cleaned_data['characters']:
				FilmCharacter.objects.create(film=film, character=character)
			for planet in form.cleaned_data['planets']:
				FilmPlanet.objects.create(film=film, planet=planet)

			return redirect(film) # shortcut to object's get_absolute_url()
			# return HttpResponseRedirect(film.get_absolute_url())

		return render(request, 'webapp/film_new.html', {'form': form})

	def get(self, request):
		form = FilmForm()
		return render(request, 'webapp/film_new.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class FilmDeleteView(generic.DeleteView):
	model = Film
	success_message = "Film deleted successfully"
	success_url = reverse_lazy('films')
	context_object_name = 'film'
	template_name = 'webapp/film_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Delete FilmJurisdiction entries
		FilmCharacter.objects \
			.filter(film_id=self.object.film_id) \
			.delete()
		FilmPlanet.objects \
			.filter(film_id=self.object.film_id) \
			.delete()

		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class FilmUpdateview(generic.UpdateView):
	model = Film
	form_class = FilmForm
	context_object_name = 'film'
	success_message = "Film updated successfully"
	template_name = 'webapp/film_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		film = form.save(commit=False)
		film.save()

		# If any existing characters are not in updated list, delete them
		new_character_ids = []
		old_character_ids = FilmCharacter.objects \
			.values_list('character_id', flat=True) \
			.filter(film_id=film.film_id)

		# New Character list
		new_characters = form.cleaned_data['characters']

		# Insert new unmatched character entries
		for character in new_characters:
			new_id = character.person_id
			new_character_ids.append(new_id)
			if new_id in old_character_ids:
				continue
			else:
				FilmCharacter.objects \
					.create(film=film, character=character)

		# Delete old unmatched character entries
		for old_character_id in old_character_ids:
			if old_character_id in new_character_ids:
				continue
			else:
				FilmCharacter.objects \
					.filter(film_id=film.film_id, character_id=old_character_id) \
					.delete()

		# If any existing planets are not in updated list, delete them
		new_planet_ids = []
		old_planet_ids = FilmPlanet.objects \
			.values_list('planet_id', flat=True) \
			.filter(film_id=film.film_id)

		# New Planet list
		new_planets = form.cleaned_data['planets']

		# Insert new unmatched planet entries
		for planet in new_planets:
			new_id = planet.planet_id
			new_planet_ids.append(new_id)
			if new_id in old_planet_ids:
				continue
			else:
				FilmPlanet.objects \
					.create(film=film, planet=planet)

		# Delete old unmatched planet entries
		for old_planet_id in old_planet_ids:
			if old_planet_id in new_planet_ids:
				continue
			else:
				FilmPlanet.objects \
					.filter(film_id=film.film_id, planet_id=old_planet_id) \
					.delete()

		# return HttpResponseRedirect(film.get_absolute_url())
		return redirect('film_detail', pk=film.pk)


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
	context_object_name = 'film'
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
			if form.cleaned_data['passengers']:
				for passenger in form.cleaned_data['passengers']:
					VehiclePassenger.objects.create(vehicle=vehicle, passenger=passenger)
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

		# Delete VehiclePassenger entries
		VehiclePassenger.objects \
			.filter(vehicle_id=self.object.vehicle_id) \
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