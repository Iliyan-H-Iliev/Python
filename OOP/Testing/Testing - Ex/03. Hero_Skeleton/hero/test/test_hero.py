from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Test", 1, 100, 100)
        self.enemy_hero = Hero("Enemy", 1, 100, 100)

    def test_init_hero(self):
        self.assertEqual("Test", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_your_health_is_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_is_zero(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        self.hero.health = 1
        self.enemy_hero.health = 1
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("Draw", result)

    def test_battle_win(self):
        self.enemy_hero.health = 1
        self.enemy_hero.damage = 1
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(104, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_lose(self):
        self.hero.health = 1
        self.hero.damage = 1
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(2, self.enemy_hero.level)
        self.assertEqual(104, self.enemy_hero.health)
        self.assertEqual(105, self.enemy_hero.damage)

    def test_str(self):
        result = str(self.hero)
        self.assertEqual("Hero Test: 1 lvl\nHealth: 100\nDamage: 100\n", result)


if __name__ == '__main__':
    main()
