from django.db import models
# from django.urls import reverse


class Person(models.Model):
    """ A person i.e., Luke Skywalker. """

    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=10, blank=True, null=True)
    species = models.ForeignKey('Species', related_name="species", on_delete=models.PROTECT, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    mass = models.CharField(max_length=10, blank=True, null=True)
    eye_color = models.CharField(max_length=20, blank=True, null=True)
    hair_color = models.CharField(max_length=20, blank=True, null=True)
    skin_color = models.CharField(max_length=20, blank=True, null=True)
    home_world = models.ForeignKey('Planet', related_name="person_home_world", on_delete=models.PROTECT, blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='people', on_delete=models.CASCADE, blank=True, null=True)

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
    """ A species i.e., droid. """

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
