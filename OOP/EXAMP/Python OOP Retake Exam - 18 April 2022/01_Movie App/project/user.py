from typing import List


from project.movie_specification.movie import Movie


class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List[Movie] = []
        self.movies_owned: List[Movie] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value.strip():
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):

        res = [f'Username: {self.username}, Age: {self.age}', 'Liked movies:']

        if self.movies_liked:
            for movie in self.movies_liked:
                res.append(movie.details())
        else:
            res.append("No movies liked.")

        res.append('Owned movies:')

        if self.movies_owned:
            for movie in self.movies_owned:
                res.append(movie.details())
        else:
            res.append('No movies owned.')

        return '\n'.join(res)
