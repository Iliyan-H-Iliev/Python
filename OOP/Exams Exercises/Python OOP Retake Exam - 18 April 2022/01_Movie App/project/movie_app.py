from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def __str__(self):
        res = f"All users: " \
              f"{', '.join([u.username for u in self.users_collection]) if self.users_collection else 'No users.'}\n"
        res += f"All movies: " \
               f"{', '.join([m.title for m in self.movies_collection]) if self.movies_collection else 'No movies.'}"

        return res

    def register_user(self, username: str, age: int):

        if self.user_not_exists(username):
            user = User(username, age)
            self.users_collection.append(user)
            return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.username_is_owner(username, movie)

        user = self.find_user(username)

        if not user:
            raise Exception(f"This user does not exist!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        self.username_is_owner(username, movie)

        for key, value in kwargs.items():
            setattr(movie, key, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        self.username_is_owner(username, movie)

        user = self.find_user(username)
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):

        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        user = self.find_user(username)

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.find_user(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):

        if not self.movies_collection:
            return "No movies found."

        return "\n".join([f"{movie.details()}"
                          for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title))])

    def user_not_exists(self, username: str):
        user = [u for u in self.users_collection if u.username == username]
        if user:
            raise Exception("User already exists!")
        return True

    def find_user(self, username: str):
        user = [u for u in self.users_collection if u.username == username]
        if not user:
            return None
        return user[0]

    @staticmethod
    def username_is_owner(username: str, movie: Movie):
        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

