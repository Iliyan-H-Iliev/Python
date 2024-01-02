from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import DirectorManager


# Create your models here.

class Person(models.Model):
    class Meta:
        abstract = True

    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default='Unknown')


class Director(Person):

    objects = DirectorManager()

    years_of_experience = models.SmallIntegerField(validators=[MinValueValidator(0)], default=0)


class Actor(Person):
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)


class Movie(models.Model):
    class GenreChoices(models.TextChoices):
        Action = 'Action'
        Comedy = 'Comedy'
        Drama = 'Drama'
        Other = 'Other'

    title = models.CharField(max_length=150, validators=[MinLengthValidator(5)])
    release_date = models.DateField()
    storyline = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=6, choices=GenreChoices.choices, default=GenreChoices.Other)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0
    )
    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(to=Director, on_delete=models.CASCADE, related_name="movies")
    starring_actor = models.ForeignKey(
        to=Actor, null=True, blank=True, on_delete=models.SET_NULL, related_name="movies"
    )
    actors = models.ManyToManyField(to=Actor)
