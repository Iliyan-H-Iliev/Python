import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Review, Article

# Import your models here
# Create and run your queries within functions


def get_authors(search_name=None, search_email=None):

    if search_name is None and search_email is None:
        return ""

    query = Q()
    query_name = Q(full_name__icontains=search_name)
    query_email = Q(email__icontains=search_email)

    if search_name and search_email:
        query = query_name & query_email
    elif search_email:
        query = query_email
    else:
        query = query_name

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
    author = Author.objects.get_authors_by_article_count().first()

    if not author:
        return ""

    return f"Top Author: {author.full_name} with {author.num_of_articles} published articles."


def get_top_reviewer():
    author = Author.objects.annotate(
        num_of_reviews=Count("reviews")
    ).order_by(
        "-num_of_reviews",
        "email"
    ).first()

    if not author or author.reviews:
        return ""

    return f"Top Reviewer: {author.full_name} with {author.num_of_reviews} published reviews."


def get_latest_article():
    article = Article.objects.annotate(
        num_of_review=Count("authors__reviews"),
        avg_rating=Avg("article__rating")
    ).order_by("published_on").last()

    if not article:
        return ""

    authors = ", ".join([author.full_name for author in article.authors.all()])

    return (f"The latest article is: {article.title}. "
            f"Authors: {authors}. "
            f"Reviewed: {article.num_of_review} times. "
            f"Average Rating: {article.avg_rating}.")


def get_top_rated_article():
    article = Article.objects.annotate(
        num_of_review=Count("authors__reviews"),
        avg_rating=Avg("article__rating")
    ).order_by("-avg_rating", "title").first()

    if not article:
        return ""

    return (f"The top-rated article is: {article.title}, "
            f"with an average rating of {article.avg_rating}, "
            f"reviewed {article.num_of_review} times.")


def ban_author(email=None):
    if email is None or not Author.objects.all():
        return "No authors banned."

    author = Author.objects.select_related("reviews").filter(email__exact=email).first()

    if not author:
        return "No authors banned."

    num_reviews = author.reviews.count()

    for review in author.reviews:
        review.delete()

    author.is_banned = True
    author.save()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."


print(get_latest_article())
