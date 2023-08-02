from project.plantation import Plantation

from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self):
        self.plantation = Plantation(2)

    def test_init(self):
        self.assertEqual(2, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_property_size(self):
        self.assertEqual(2, self.plantation.size)

    def test_size_setter_with_negative_value(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_size_setter_with_zero(self):
        self.plantation.size = 0
        self.assertEqual(0, self.plantation.size)

    def test_size_setter_with_positive_value(self):
        self.plantation.size = 10
        self.assertEqual(10, self.plantation.size)

    def test_hire_worker_with_worker_not_in_workers(self):
        message = self.plantation.hire_worker("Pesho")
        self.assertEqual("Pesho successfully hired.", message)
        self.assertEqual(["Pesho"], self.plantation.workers)

    def test_hire_worker_with_worker_in_workers(self):
        self.plantation.workers = ["Pesho"]
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Pesho")
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_len(self):
        self.plantation.plants = {"Pesho": ["Apple", "Cherry", "Banana"]}
        self.assertEqual(3, len(self.plantation))

    def test_len_with_more_than_one_worker(self):
        self.plantation.plants = {"Pesho": ["Apple", "Cherry", "Banana"], "Gosho": ["Apple", "Cherry", "Banana"]}
        self.assertEqual(6, len(self.plantation))

    def test_len_with_empty_plants(self):
        self.assertEqual(0, len(self.plantation))

    def test_planting_with_worker_not_in_workers(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Pesho", "Apple")
        self.assertEqual("Worker with name Pesho is not hired!", str(ex.exception))

    def test_planting_with_len_of_plants_greater_than_size(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.plants = {"Pesho": ["Apple", "Cherry"]}
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Pesho", "Apple")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_with_worker_in_workers_and_plant_in_plants(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.plants = {"Pesho": ["Apple"]}
        message = self.plantation.planting("Pesho", "Cherry")
        self.assertEqual("Pesho planted Cherry.", message)
        self.assertEqual({"Pesho": ["Apple", "Cherry"]}, self.plantation.plants)

    def test_planting_with_worker_in_workers_and_plant_not_in_plants(self):
        self.plantation.workers = ["Pesho"]
        message = self.plantation.planting("Pesho", "Cherry")
        self.assertEqual("Pesho planted it's first Cherry.", message)
        self.assertEqual({"Pesho": ["Cherry"]}, self.plantation.plants)

    def test_str(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.plants = {"Pesho": ["Apple", "Cherry"]}
        message = str(self.plantation)
        self.assertEqual("Plantation size: 2\nPesho\nPesho planted: Apple, Cherry", message)

    def test_repr(self):
        self.plantation.workers = ["Pesho"]
        self.plantation.plants = {"Pesho": ["Apple", "Cherry"]}
        message = repr(self.plantation)
        self.assertEqual("Size: 2\nWorkers: Pesho", message)


if __name__ == '__main__':
    main()