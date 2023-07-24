from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50.5, 150.2)

    def test_attributes(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init(self):
        self.assertEqual(50.5, self.vehicle.fuel)
        self.assertEqual(50.5, self.vehicle.capacity)
        self.assertEqual(150.2, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive(self):
        self.vehicle.drive(10)
        self.assertEqual(38, self.vehicle.fuel)

    def test_drive_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(10)
        self.assertEqual(48, self.vehicle.fuel)

    def test_refuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        self.assertEqual("The vehicle has 150.2 horse power with 50.5 fuel left and 1.25 fuel consumption",
                         str(self.vehicle))


if __name__ == "__main__":
    main()
