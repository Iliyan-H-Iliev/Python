from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "Test type", "Test sound")

    def test_init(self):
        self.assertEqual(self.mammal.name, "Test")
        self.assertEqual(self.mammal.type, "Test type")
        self.assertEqual(self.mammal.sound, "Test sound")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Test makes Test sound")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.mammal.info(), "Test is of type Test type")


if __name__ == "__main__":
    main()
