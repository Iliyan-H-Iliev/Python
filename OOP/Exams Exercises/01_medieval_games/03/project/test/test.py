# from project.movie import Movie
# from unittest import TestCase, main
#
#
# class TestMovie(TestCase):
#     def setUp(self):
#         self.movie = Movie("Test", 2020, 5.5)
#
#     def test_init(self):
#         self.assertEqual(self.movie.name, "Test")
#         self.assertEqual(self.movie.year, 2020)
#         self.assertEqual(self.movie.rating, 5.5)
#         self.assertEqual(self.movie.actors, [])
#
#     def test_name_getter(self):
#         self.assertEqual(self.movie.name, "Test")
#
#     def test_name_setter_with_valid_input(self):
#         self.movie.name = "New"
#         self.assertEqual(self.movie.name, "New")
#
#     def test_name_setter_with_not_valid_input(self):
#         with self.assertRaises(ValueError) as ex:
#             self.movie.name = ""
#         self.assertEqual(str(ex.exception), "Name cannot be an empty string!")
#
#     def test_year_getter(self):
#         self.assertEqual(self.movie.year, 2020)
#
#     def test_year_setter_with_valid_input(self):
#         self.movie.year = 2021
#         self.assertEqual(self.movie.year, 2021)
#
#     def test_year_setter_with_not_valid_input(self):
#         with self.assertRaises(ValueError) as ex:
#             self.movie.year = 1886
#         self.assertEqual(str(ex.exception), "Year is not valid!")
#
#     def test_add_actor_with_valid_input(self):
#         self.movie.add_actor("Actor")
#         self.assertEqual(self.movie.actors, ["Actor"])
#
#     def test_add_actor_already_added(self):
#         self.movie.add_actor("Actor")
#         self.assertEqual(self.movie.add_actor("Actor"), "Actor is already added in the list of actors!")
#
#     def test_repr_without_actors(self):
#         self.assertEqual(self.movie.__repr__(), "Name: Test\nYear of Release: 2020\nRating: 5.50\nCast: ")
#
#     def test_repr(self):
#         self.movie.add_actor("Actor")
#         self.movie.add_actor("Actor2")
#         self.assertEqual(self.movie.__repr__(), "Name: Test\nYear of Release: 2020\nRating: 5.50\nCast: Actor, Actor2")
#
#     def test_movie_2_gt(self):
#         movie2 = Movie("Test2", 2020, 6.5)
#         self.assertEqual(self.movie.__gt__(movie2), '"Test2" is better than "Test"')
#
#     def test_movie_1_gt(self):
#         movie2 = Movie("Test2", 2020, 4.5)
#         self.assertEqual(self.movie.__gt__(movie2), '"Test" is better than "Test2"')
#
#
# if __name__ == "__main__":
#     main()


from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Test", 1999, 9.5)

    def test_correct_initializing(self):
        self.assertEqual("Test", self.movie.name)
        self.assertEqual(1999, self.movie.year)
        self.assertEqual(9.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_error_rising_not_valid_name(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_error_rising_valid_name(self):
        self.movie.name = "New Name"

        self.assertEqual("New Name", self.movie.name)

    def test_error_rising_not_valid_year(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1858

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_functionality(self):
        self.assertEqual([], self.movie.actors)

        self.movie.add_actor("Test Actor")
        self.movie.add_actor("Test Actress")

        self.assertEqual(["Test Actor", "Test Actress"], self.movie.actors)

    def test_add_existing_actor(self):
        self.movie.add_actor("Test Actor")
        self.movie.add_actor("Test Actress")

        result = self.movie.add_actor("Test Actor")

        self.assertEqual("Test Actor is already added in the list of actors!", result)

    def test_first_movie_better_than_other_movie(self):
        other_movie = Movie("Test2", 1998, 9.4)

        result = self.movie > other_movie

        self.assertEqual('"Test" is better than "Test2"', result)

    def test_other_movie_better_than_first_movie(self):
        other_movie = Movie("Test2", 1998, 9.6)

        result = self.movie > other_movie

        self.assertEqual('"Test2" is better than "Test"', result)

    def test_representation_functionality(self):
        self.movie.add_actor("Test Actor")
        self.movie.add_actor("Test Actress")

        expect = "Name: Test\n" \
                 "Year of Release: 1999\n" \
                 "Rating: 9.50\n" \
                 "Cast: Test Actor, Test Actress"

        result = self.movie.__repr__()

        self.assertEqual(expect, result)


if __name__ == "__main__":
    main()
