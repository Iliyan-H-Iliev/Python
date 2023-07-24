from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player = TennisPlayer('Rafael Nadal', 34, 10245.5)

    def test_init(self):
        self.assertEqual(self.player.name, 'Rafael Nadal')
        self.assertEqual(self.player.age, 34)
        self.assertEqual(self.player.points, 10245.5)
        self.assertEqual(self.player.wins, [])

    def test_property_name(self):
        self.assertEqual(self.player.name, 'Rafael Nadal')

    def test_property_age(self):
        self.assertEqual(self.player.age, 34)

    def test_name_setter_with_two_symbols(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = 'Ra'
        self.assertEqual(str(ex.exception), 'Name should be more than 2 symbols!')

    def test_name_setter_without_symbols(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = ''
        self.assertEqual(str(ex.exception), 'Name should be more than 2 symbols!')

    def test_age_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 17
        self.assertEqual(str(ex.exception), 'Players must be at least 18 years of age!')

    def test_add_not_exist_new_win(self):
        self.player.add_new_win('Roland Garros')
        self.assertEqual(self.player.wins, ['Roland Garros'])

    def test_add_exist_new_win(self):
        self.player.add_new_win('Roland Garros')
        self.assertEqual(self.player.add_new_win('Roland Garros'), 'Roland Garros has been already added to the list '
                                                                   'of wins!')

    def test_lt(self):
        other_player = TennisPlayer('Roger Federer', 39, 10305.5)
        self.assertEqual(self.player < other_player, 'Roger Federer is a top seeded player and he/she is better than '
                                                     'Rafael Nadal')

    def test_lt_other(self):
        other_player = TennisPlayer('Roger Federer', 39, 10105.5)
        self.assertEqual('Rafael Nadal is a better player than Roger Federer', self.player < other_player,)

    def test_str(self):
        self.player.add_new_win('Roland Garros')
        self.player.add_new_win('Wimbledon')
        self.assertEqual(str(self.player), 'Tennis Player: Rafael Nadal\nAge: 34\nPoints: 10245.5\nTournaments won: '
                                           'Roland Garros, Wimbledon')


if __name__ == '__main__':
    main()
