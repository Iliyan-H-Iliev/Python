import os
import django
from django.db.models import Q, Count, Avg


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review


# Import your models here
# Create and run your queries within functions


def get_authors(search_name=None, search_email=None):
    query = Q()
    query_name = Q(full_name__icontains=search_name)
    query_email = Q(email__icontains=search_email)

    if search_name is not None and search_email is not None:
        query = query_name & query_email
    elif search_name is not None:
        query = query_name
    elif search_email is not None:
        query = query_email
    else:
        return ""

    authors = Author.objects.filter(query).order_by("-full_name")

    if not authors:
        return ""

    res = []

    for author in authors:
        banned = "Not Banned"
        if author.is_banned:
            banned = "Banned"

        res.append(f"Author: {author.full_name}, email: {author.email}, status: {banned}")

    return "\n".join(res)


def get_top_publisher():
    if not Article.objects.all():
        return ""

    author = Author.objects.get_authors_by_article_count().filter(num_of_articles__gt=0).first()

    if not author:
        return ""

    return f"Top Author: {author.full_name} with {author.num_of_articles} published articles."


def get_top_reviewer():
    author = Author.objects.annotate(
        num_of_reviews=Count("reviews")
    ).filter(
        num_of_reviews__gt=0
    ).order_by(
        "-num_of_reviews", "email"
    ).first()

    if not author:
        return ""

    return f"Top Reviewer: {author.full_name} with {author.num_of_reviews} published reviews."


def get_latest_article():

    article = Article.objects.prefetch_related(
        "authors"
    ).annotate(
        num_reviews=Count("reviews"),
        avg_rating=Avg("reviews__rating")
    ).order_by(
        "-published_on"
    ).first()

    if not article:
        return ""

    avg_rating = article.avg_rating

    if article.avg_rating is None:
        avg_rating = 0

    authors = ", ".join([author.full_name for author in article.authors.all()])

    return (f"The latest article is: {article.title}. "
            f"Authors: {authors}. "
            f"Reviewed: {article.num_reviews} times. "
            f"Average Rating: {avg_rating:.2f}.")


def get_top_rated_article():
    article = Article.objects.annotate(
        num_reviews=Count("reviews"),
        avg_rating=Avg("reviews__rating")
    ).filter(
        avg_rating__gt=0
    ).order_by(
        "-avg_rating", "title"
    ).first()

    if not article:
        return ""

    return (f"The top-rated article is: {article.title}, "
            f"with an average rating of {article.avg_rating:.2f}, "
            f"reviewed {article.num_reviews} times.")


def ban_author(email=None):
    if email is None or not Author.objects.all():
        return "No authors banned."

    author = Author.objects.prefetch_related(
        "reviews"
    ).annotate(
        num_reviews=Count("reviews")
    ).filter(
        email__exact=email
    ).first()

    if not author:
        return "No authors banned."

    for review in author.reviews.all():
        review.delete()

    author.is_banned = True
    author.save()

    return f"Author: {author.full_name} is banned! {author.num_reviews} reviews deleted."
