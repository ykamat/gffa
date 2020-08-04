from django.db import models
from django.urls import reverse


class Person(models.Model):
    """ A person i.e., Luke Skywalker. """

    person_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=10, null=True)
    height = models.CharField(max_length=10, null=True)
    mass = models.CharField(max_length=10, null=True)
    eye_color = models.CharField(max_length=20, null=True)
    hair_color = models.CharField(max_length=20, null=True)
    skin_color = models.CharField(max_length=20, null=True)
    # homeworld = models.ForeignKey(Planet, related_name="residents", on_delete=models.PROTECT, null=True)

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
