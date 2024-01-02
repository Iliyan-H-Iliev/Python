import os
import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie


# Import your models here
# Create and run your queries within functions


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    query = Q()
    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name and search_nationality:
        query = query_name & query_nationality
    elif search_nationality:
        query = query_nationality
    else:
        query = query_name

    directors = Director.objects.filter(query).order_by("full_name")

    if not directors:
        return ""

    return "\n".join(f"Director: {director.full_name}, "
                     f"nationality: {director.nationality}, "
                     f"experience: {director.years_of_experience}"
                     for director in directors)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ""

    return f"Top Director: {director.full_name}, movies: {director.movies_count}."


def get_top_actor():
    actor = Actor.objects.prefetch_related("movies").annotate(
        num_movies=Count("movies"),
        avg_rating=Avg("movies__rating")
    ).order_by("-num_movies", "full_name").first()

    if not actor or not actor.num_movies:
        return ""

    movies = ", ".join([movie.title for movie in actor.movies.all()])

    return (f"Top Actor: {actor.full_name}, "
            f"starring in movies: {movies}, "
            f"movies average rating: {actor.avg_rating:.1f}")


def get_actors_by_movies_count():

    if Movie.objects.all().count() == 0:
        return ""

    actors = (Actor.objects.
              annotate(num_movies=Count("movie")).
              order_by("-num_movies", "full_name"))[:3]

    if not actors:
        return ""

    return "\n".join(f"{actor.full_name}, participated in {actor.num_movies} movies" for actor in actors)


def get_top_rated_awarded_movie():
    movie = (Movie.objects.select_related("starring_actor").
             prefetch_related("actors").
             filter(is_awarded=True).
             order_by("-rating", "title").
             first())

    if movie is None:
        return ""

    actors = ", ".join([actor.full_name for actor in movie.actors.order_by("full_name")])
    starring_actor_full_name = movie.starring_actor.full_name if movie.starring_actor else "N/A"

    return (f"Top rated awarded movie: {movie.title}, rating: {movie.rating:.1f}. "
            f"Starring actor: {starring_actor_full_name}. "
            f"Cast: {actors}.")


def increase_rating():
    movies = Movie.objects.filter(rating__lt=10.0, is_classic=True)

    if not movies:
        return "No ratings increased."

    count = movies.update(rating=F("rating") + 0.1)

    return f"Rating increased for {count} movies."

