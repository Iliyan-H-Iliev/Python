from project.second_hand_car import SecondHandCar
from unittest import TestCase, main

class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar('BMW', 'X5', 1000, 10000)

    def test_init(self):
        self.assertEqual(self.car.model, 'BMW')
        self.assertEqual(self.car.car_type, 'X5')
        self.assertEqual(self.car.mileage, 1000)
        self.assertEqual(self.car.price, 10000)
        self.assertEqual(self.car.repairs, [])

    def test_price_setter_with_invalid_value(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 1
        self.assertEqual(str(ex.exception), 'Price should be greater than 1.0!')

    def test_mileage_setter_with_invalid_value(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotional_price_with_invalid_value(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(100000)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    def test_set_promotional_price_with_valid_value(self):
        self.assertEqual(self.car.set_promotional_price(5000), 'The promotional price has been successfully set.')
        self.assertEqual(self.car.price, 5000)

    def test_need_repair_with_invalid_value(self):
        self.assertEqual(self.car.need_repair(5001, 'broken engine'), 'Repair is impossible!')
        self.assertEqual(self.car.price, 10000)
        self.assertEqual(self.car.repairs, [])

    def test_need_repair_with_valid_value(self):
        self.assertEqual(self.car.need_repair(5000, 'broken engine'), 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 15000)
        self.assertEqual(self.car.repairs, ['broken engine'])

    def test_gt_with_invalid_car_type(self):
        other_car = SecondHandCar('BMW', 'X3', 1000, 10000)
        self.assertEqual(self.car > other_car, 'Cars cannot be compared. Type mismatch!')

    def test_gt_with_valid_car_type(self):
        other_car = SecondHandCar('BMW', 'X5', 1000, 9500)
        self.assertTrue(self.car > other_car)

    def test_lt_with_valid_car_type(self):
        other_car = SecondHandCar('BMW', 'X5', 1000, 10500)
        self.assertFalse(self.car > other_car)

    def test_str(self):
        self.assertEqual(str(self.car), f'Model BMW | Type X5 | Milage 1000km\n'
                                        f'Current price: 10000.00 | Number of Repairs: 0')


if __name__ == '__main__':
    main()

