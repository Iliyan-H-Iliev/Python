from project.factory.paint_factory import PaintFactory
from unittest import TestCase, main


class TestPaintFactory(TestCase):

    def setUp(self):
        self.paint_factory = PaintFactory("Test", 100)

    def test_init(self):
        self.assertEqual("Test", self.paint_factory.name)
        self.assertEqual(100, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)

    def test_can_add_with_enough_space(self):
        self.assertTrue(self.paint_factory.can_add(10))

    def test_can_add_with_not_enough_space(self):
        self.paint_factory.add_ingredient("white", 90)
        self.assertFalse(self.paint_factory.can_add(11))

    def test_add_ingredient_with_valid_ingredient_and_enough_space(self):
        self.paint_factory.add_ingredient("white", 10)
        self.assertEqual({"white": 10}, self.paint_factory.ingredients)

    def test_add_ingredient_with_valid_ingredient_and_not_enough_space(self):
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("white", 101)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_with_invalid_ingredient(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("black", 10)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_with_valid_ingredient_and_quantity_equal_to_capacity(self):
        self.paint_factory.add_ingredient("white", 100)
        self.assertEqual({"white": 100}, self.paint_factory.ingredients)

    def test_add_exist_ingredient(self):
        self.paint_factory.add_ingredient("white", 10)
        self.paint_factory.add_ingredient("white", 10)
        self.assertEqual({"white": 20}, self.paint_factory.ingredients)

    def test_remove_ingredient_with_valid_ingredient_and_quantity(self):
        self.paint_factory.add_ingredient("white", 10)
        self.paint_factory.remove_ingredient("white", 5)
        self.assertEqual({"white": 5}, self.paint_factory.ingredients)

    def test_remove_ingredient_with_valid_ingredient_and_quantity_equal_to_0(self):
        self.paint_factory.add_ingredient("white", 10)
        self.paint_factory.remove_ingredient("white", 10)
        self.assertEqual({"white": 0}, self.paint_factory.ingredients)

    def test_remove_ingredient_with_valid_ingredient_and_bigger_quantity(self):
        self.paint_factory.add_ingredient("white", 10)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("white", 11)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_with_invalid_ingredient(self):
        self.paint_factory.add_ingredient("white", 10)
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient("black", 10)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_products_property(self):
        self.paint_factory.add_ingredient("white", 10)
        self.assertEqual({"white": 10}, self.paint_factory.products)

    def test_repr_method(self):
        self.paint_factory.add_ingredient("white", 10)
        self.paint_factory.add_ingredient("yellow", 15)
        expected = "Factory name: Test with capacity 100.\nwhite: 10\nyellow: 15\n"
        self.assertEqual(expected, self.paint_factory.__repr__())


if __name__ == "__main__":
    main()