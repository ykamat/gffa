from django.db import models
# from django.urls import reverse


class Film(models.Model):
    """ A film i.e. The Empire Strikes Back """

    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    episode_id = models.IntegerField(blank=True, null=True)
    opening_crawl = models.TextField(max_length=1000, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    producer = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    characters = models.ManyToManyField('Person', through='FilmPerson', related_name='film_person', blank=True)
    # planets = models.ManyToManyField('Planet', related_name="film_planets", blank=True)
    # starships = models.ManyToManyField('Starship', related_name="film_starships", blank=True)
    # vehicles = models.ManyToManyField('Vehicle', related_name="film_vehicles", blank=True)
    # species = models.ManyToManyField('Species', related_name="film_species", blank=True)

    def get_characters(self):
        return "\n".join([character.name for character in self.characters.all()])
    
    # def get_planets(self):
    #     return "\n".join([planet.url for planet in self.planets.all()])

    # def get_starships(self):
    #     return "\n".join([starship.url for starship in self.starships.all()])

    # def get_vehicles(self):
    #     return "\n".join([vehicle.url for vehicle in self.vehicles.all()])

    # def get_species(self):
    #     return "\n".join([species.url for species in self.species.all()])

    class Meta:
        managed = True
        db_table = 'film'
        ordering = ['title']
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    # def get_absolute_url(self):
    #     return reverse('person_detail', args=[self.url])

    # def __unicode__(self):
    #     return self.name

    def __str__(self):
        return self.title


class Person(models.Model):
    """ A person i.e., Luke Skywalker. """

    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=10, blank=True, null=True)
    species = models.ForeignKey('Species', related_name="person_species", on_delete=models.PROTECT, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    mass = models.CharField(max_length=10, blank=True, null=True)
    eye_color = models.CharField(max_length=20, blank=True, null=True)
    hair_color = models.CharField(max_length=20, blank=True, null=True)
    skin_color = models.CharField(max_length=20, blank=True, null=True)
    home_world = models.ForeignKey('Planet', related_name="person_home_world", on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'person'
        ordering = ['name']
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    # def get_absolute_url(self):
    #     return reverse('person_detail', args=[self.url])

    # def __unicode__(self):
    #     return self.name

    def __str__(self):
        return self.name


class Planet(models.Model):
    """ A planet i.e. Tatooine """

    planet_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rotation_period = models.CharField(max_length=40, blank=True, null=True)
    orbital_period = models.CharField(max_length=40, blank=True, null=True)
    diameter = models.CharField(max_length=40, blank=True, null=True)
    climate = models.CharField(max_length=40, blank=True, null=True)
    gravity = models.CharField(max_length=40, blank=True, null=True)
    terrain = models.CharField(max_length=40, blank=True, null=True)
    surface_water = models.CharField(max_length=40, blank=True, null=True)
    population = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planet'
        ordering = ['name']
        verbose_name = 'Planet'
        verbose_name_plural = 'Planets'

    # def __unicode__(self):
    #     return self.name

    def __str__(self):
        return self.name


class Species(models.Model):
    """ A species i.e. droid. """

    species_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    classification = models.CharField(max_length=40, blank=True, null=True)
    designation = models.CharField(max_length=40, blank=True, null=True)
    average_height = models.CharField(max_length=40, blank=True, null=True)
    skin_colors = models.CharField(max_length=200, blank=True, null=True)
    hair_colors = models.CharField(max_length=200, blank=True, null=True)
    eye_colors = models.CharField(max_length=200, blank=True, null=True)
    average_lifespan = models.CharField(max_length=40, blank=True, null=True)
    language = models.CharField(max_length=40, blank=True, null=True)
    home_world = models.ForeignKey('Planet', related_name="species_home_world", on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'species'
        ordering = ['name']
        verbose_name = 'Species'
        verbose_name_plural = 'Species'

    # def get_absolute_url(self):
    #     return reverse('species_detail', args=[self.url])

    # def __unicode__(self):
    #     return self.name

    def __str__(self):
        return self.name


class Starship(models.Model):
    """ A starship i.e. Death Star """

    starship_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    starship_class = models.CharField(max_length=40, blank=True, null=True)
    manufacturer = models.CharField(max_length=40, blank=True, null=True)
    cost_in_credits = models.CharField(max_length=40, blank=True, null=True)
    length = models.CharField(max_length=40, blank=True, null=True)
    crew = models.CharField(max_length=40, blank=True, null=True)
    passengers = models.CharField(max_length=40, blank=True, null=True)
    max_atmosphering_speed = models.CharField(max_length=40, blank=True, null=True)
    hyperdrive_rating = models.CharField(max_length=40, blank=True, null=True)
    MGLT = models.CharField(max_length=40, blank=True, null=True)
    cargo_capacity = models.CharField(max_length=40, blank=True, null=True)
    consumables = models.CharField(max_length=40, blank=True, null=True)
    pilots = models.ForeignKey('Person', related_name='starship_person', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'starship'
        ordering = ['name']
        verbose_name = 'Starship'
        verbose_name_plural = 'Starships'

    # def __unicode__(self):
    #     return self.name

    def __str__(self):
        return self.name


class Vehicles(models.Model):
    """ A vehicle, i.e. Snowspeeder. """

    vehicles_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    vehicle_class = models.CharField(max_length=40, blank=True, null=True)
    manufacturer = models.CharField(max_length=40, blank=True, null=True)
    length = models.CharField(max_length=40, blank=True, null=True)
    cost_in_credits = models.CharField(max_length=40, blank=True, null=True)
    crew = models.CharField(max_length=40, blank=True, null=True)
    passengers = models.CharField(max_length=40, blank=True, null=True)
    max_atmosphering_speed = models.CharField(max_length=40, blank=True, null=True)
    cargo_capacity = models.CharField(max_length=40, blank=True, null=True)
    consumables = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vehicles'
        ordering = ['name']
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
    
    def __str___(self):
        return self.name


class FilmPerson(models.Model):
    # film_person_id = models.AutoField(primary_key=True)
    film = models.ForeignKey('Film', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    
