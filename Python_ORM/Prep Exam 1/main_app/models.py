from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import TennisPlayerManager


# Create your models here.


class TennisPlayer(models.Model):

    objects = TennisPlayerManager()

    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(5)])
    birth_date = models.DateField()
    country = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    ranking = models.PositiveIntegerField(validators=[MinValueValidator(1), MinValueValidator(300)])
    is_active = models.BooleanField(default=True)


class Tournament(models.Model):
    class SurfaceTypeChoice(models.TextChoices):
        Not_Selected = "Not Selected",
        Clay = "Clay",
        Grass = "Grass",
        Hard_Court = "Hard Court"

    name = models.CharField(max_length=150, validators=[MinLengthValidator(2)], unique=True)
    location = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    prize_money = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    surface_type = models.CharField(
        max_length=12,
        choices=SurfaceTypeChoice.choices,
        default=SurfaceTypeChoice.Not_Selected)


class Match(models.Model):

    class Meta:
        verbose_name_plural = "Matches"

    score = models.CharField(max_length=100)
    summary = models.TextField(validators=[MinLengthValidator(5)])
    date_played = models.DateTimeField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="matches")
    players = models.ManyToManyField(TennisPlayer, related_name="matches")
    winner = models.ForeignKey(
        TennisPlayer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="match_winner"
    )
