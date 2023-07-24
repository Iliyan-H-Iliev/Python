from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Test", 2020, 5.5)

    def test_init(self):
        self.assertEqual(self.movie.name, "Test")
        self.assertEqual(self.movie.year, 2020)
        self.assertEqual(self.movie.rating, 5.5)
        self.assertEqual(self.movie.actors, [])

    def test_name_getter(self):
        self.assertEqual(self.movie.name, "Test")

    def test_name_setter_with_valid_input(self):
        self.movie.name = "New"
        self.assertEqual(self.movie.name, "New")

    def test_name_setter_with_not_valid_input(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""
        self.assertEqual(str(ex.exception), "Name cannot be an empty string!")

    def test_year_getter(self):
        self.assertEqual(self.movie.year, 2020)

    def test_year_setter_with_valid_input(self):
        self.movie.year = 2021
        self.assertEqual(self.movie.year, 2021)

    def test_year_setter_with_not_valid_input(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1886
        self.assertEqual(str(ex.exception), "Year is not valid!")

    def test_add_actor_with_valid_input(self):
        self.movie.add_actor("Actor")
        self.assertEqual(self.movie.actors, ["Actor"])

    def test_add_actor_already_added(self):
        self.movie.add_actor("Actor")
        self.assertEqual(self.movie.add_actor("Actor"), "Actor is already added in the list of actors!")

    def test_repr_without_actors(self):
        self.assertEqual(self.movie.__repr__(), "Name: Test\nYear of Release: 2020\nRating: 5.50\nCast: ")

    def test_repr(self):
        self.movie.add_actor("Actor")
        self.movie.add_actor("Actor2")
        self.assertEqual(self.movie.__repr__(), "Name: Test\nYear of Release: 2020\nRating: 5.50\nCast: Actor, Actor2")

    def test_movie_2_gt(self):
        movie2 = Movie("Test2", 2020, 6.5)
        self.assertEqual(self.movie.__gt__(movie2), '"Test2" is better than "Test"')

    def test_movie_1_gt(self):
        movie2 = Movie("Test2", 2020, 4.5)
        self.assertEqual(self.movie.__gt__(movie2), '"Test" is better than "Test2"')


if __name__ == "__main__":
    main()
