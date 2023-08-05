from unittest import TestCase, main
from project.pet_shop import PetShop


class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.pet_shop = PetShop("Test")

    def test_init(self):
        self.assertEqual("Test", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_quantity_less_than_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("Test", -1)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_add_food_name_not_in_food(self):
        self.assertEqual("Successfully added 1.00 grams of Test.", self.pet_shop.add_food("Test", 1))
        self.assertEqual("Successfully added 1.00 grams of Test1.", self.pet_shop.add_food("Test1", 1))
        self.assertEqual({"Test": 1, "Test1": 1}, self.pet_shop.food)

    def test_add_food_name_in_food(self):
        self.pet_shop.food = {"Test": 1, "Test1": 1}
        self.assertEqual("Successfully added 1.00 grams of Test.", self.pet_shop.add_food("Test", 1))
        self.assertEqual("Successfully added 1.00 grams of Test1.", self.pet_shop.add_food("Test1", 1))
        self.assertEqual({"Test": 2, "Test1": 2}, self.pet_shop.food)

    def test_add_pet_name_not_in_pets(self):
        self.assertEqual("Successfully added Test.", self.pet_shop.add_pet("Test"))
        self.assertEqual(["Test"], self.pet_shop.pets)

    def test_add_pet_name_in_pets(self):
        self.pet_shop.pets = ["Test"]
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Test")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_name_not_in_pets(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Test", "Test")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_food_name_not_in_food(self):
        self.pet_shop.pets = ["Test"]
        self.assertEqual("You do not have Test", self.pet_shop.feed_pet("Test", "Test"))

    def test_feed_pet_food_quantity_less_than_100(self):
        self.pet_shop.pets = ["Test"]
        self.pet_shop.food = {"Test": 1}
        self.assertEqual("Adding food...", self.pet_shop.feed_pet("Test", "Test"))
        self.assertEqual({"Test": 1001}, self.pet_shop.food)

    def test_feed_pet_food_quantity_greater_than_100(self):
        self.pet_shop.pets = ["Test"]
        self.pet_shop.food = {"Test": 101}
        self.assertEqual("Test was successfully fed", self.pet_shop.feed_pet("Test", "Test"))
        self.assertEqual({"Test": 1}, self.pet_shop.food)

    def test_repr(self):
        self.pet_shop.pets = ["Test"]
        self.assertEqual("Shop Test:\nPets: Test", self.pet_shop.__repr__())


if __name__ == '__main__':
    main()

