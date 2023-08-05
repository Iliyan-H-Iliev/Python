from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):

    def setUp(self):
        self.robot = Robot("1", "Military", 100, 1000)

    def test_robot_init(self):
        self.assertEqual("1", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(1000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_robot_init_with_negative_price(self):
        with self.assertRaises(ValueError) as ex:
            Robot("1", "Military", 100, -1000)
        self.assertEqual("Price cannot be negative!", str(ex.exception))

    def test_robot_init_with_invalid_category(self):
        with self.assertRaises(ValueError) as ex:
            Robot("1", "Invalid", 100, 1000)
        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ex.exception))

    def test_robot_upgrade_with_already_existing_hardware(self):
        self.robot.hardware_upgrades.append("hardware")
        result = self.robot.upgrade("hardware", 100)
        self.assertEqual("Robot 1 was not upgraded.", result)

    def test_robot_upgrade_with_non_existing_hardware(self):
        result = self.robot.upgrade("hardware", 100)
        self.assertEqual("Robot 1 was upgraded with hardware.", result)
        self.assertEqual(["hardware"], self.robot.hardware_upgrades)
        self.assertEqual(1000 + 100 * 1.5, self.robot.price)

    def test_robot_update_with_already_existing_version(self):
        self.robot.software_updates.append(1.0)
        result = self.robot.update(1.0, 100)
        self.assertEqual("Robot 1 was not updated.", result)

    def test_robot_update_with_not_enough_capacity(self):
        result = self.robot.update(1.0, 200)
        self.assertEqual("Robot 1 was not updated.", result)

    def test_robot_update_with_valid_data(self):
        result = self.robot.update(1.0, 100)
        self.assertEqual("Robot 1 was updated to version 1.0.", result)
        self.assertEqual([1.0], self.robot.software_updates)
        self.assertEqual(0, self.robot.available_capacity)

    def test_robot_gt_with_greater_price(self):
        other = Robot("2", "Military", 100, 500)
        result = self.robot > other
        self.assertEqual("Robot with ID 1 is more expensive than Robot with ID 2.", result)

    def test_robot_gt_with_equal_price(self):
        other = Robot("2", "Military", 100, 1000)
        result = self.robot > other
        self.assertEqual("Robot with ID 1 costs equal to Robot with ID 2.", result)

    def test_robot_gt_with_smaller_price(self):
        other = Robot("2", "Military", 100, 1500)
        result = self.robot > other
        self.assertEqual("Robot with ID 1 is cheaper than Robot with ID 2.", result)


if __name__ == '__main__':
    main()

