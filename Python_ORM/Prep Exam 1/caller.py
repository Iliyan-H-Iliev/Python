import os
import django
from django.db.models import Q, Count


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import TennisPlayer, Tournament, Match
# Import your models here
# Create and run your queries within functions


def get_tennis_players(search_name=None, search_country=None):

    query = Q()
    query_name = Q(full_name__icontains=search_name)
    query_country = Q(country__icontains=search_country)

    if search_name is not None and search_country is not None:
        query = query_name & query_country
    elif search_name is not None:
        query = query_name
    elif search_country is not None:
        query = query_country
    else:
        return ""

    players = TennisPlayer.objects.filter(query).order_by("ranking")

    if not players:
        return ""

    res = []

    for player in players:
        res.append(f"Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}")

    return "\n".join(res)


def get_top_tennis_player():
    player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if not player:
        return ""

    return f"Top Tennis Player: {player.full_name} with {player.wins_count} wins."


def get_tennis_player_by_matches_count():
    player = (TennisPlayer.objects.annotate(
        num_of_matches=Count("matches")
    ).filter(
        num_of_matches__gt=0
    ).order_by(
        "-num_of_matches",
        "ranking"
    ).first())

    if not player:
        return ""

    return f"Tennis Player: {player.full_name} with {player.num_of_matches} matches played."


def get_tournaments_by_surface_type(surface=None):

    if surface is None:
        return ""

    tournaments = Tournament.objects.annotate(
        num_matches=Count("matches")
    ).filter(
        surface_type__icontains=surface
    ).order_by(
        "-start_date"
    )

    if not tournaments:
        return ""

    return "\n".join([f"Tournament: {tournament.name}, "
                      f"start date: {tournament.start_date}, "
                      f"matches: {tournament.num_matches}" for tournament in tournaments])


def get_latest_match_info():
    match = Match.objects.prefetch_related(
        "players"
    ).select_related(
        "winner", "tournament"
    ).order_by(
        "-date_played",
        "-id"
    ).first()

    if not match:
        return ""

    players = " vs ".join([player.full_name for player in match.players.all().order_by("full_name")])
    winner = match.winner.full_name if match.winner else "TBA"

    return (f"Latest match played on: {match.date_played}, "
            f"tournament: {match.tournament.name}, "
            f"score: {match.score}, "
            f"players: {players}, "
            f"winner: {winner}, "
            f"summary: {match.summary}")


def get_matches_by_tournament(tournament_name=None):

    if tournament_name is None or not Tournament.objects.all():
        return "No matches found."

    tournaments = Tournament.objects.prefetch_related(
        "matches",
    ).filter(
        name__exact=tournament_name
    )

    if not tournaments:
        return "No matches found."

    res = []

    for tournament in tournaments:
        if not tournament.matches.all():
            return "No matches found."
        for match in tournament.matches.all().order_by("-date_played"):
            winner = match.winner.full_name if match.winner else "TBA"

            res.append(f"Match played on: {match.date_played}, "
                       f"score: {match.score}, "
                       f"winner: {winner}")

    return "\n".join(res)