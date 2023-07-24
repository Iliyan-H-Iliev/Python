from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def __str__(self):
        return "\n".join([s.details() for s in self.services])

    def add_service(self, service_type: str, name: str):

        services = {
            "MainService": MainService,
            "SecondaryService": SecondaryService
        }

        if service_type not in ["MainService", "SecondaryService"]:
            raise Exception("Invalid service type!")

        service = services[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        robots = {
            "FemaleRobot": FemaleRobot,
            "MaleRobot": MaleRobot
        }

        if robot_type not in ["FemaleRobot", "MaleRobot"]:
            raise Exception("Invalid robot type!")

        robot = robots[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_robot_by_name(robot_name)
        service = self.find_service_by_name(service_name)

        robot_class = robot.__class__.__name__
        service_class = service.__class__.__name__

        if (robot_class == "FemaleRobot" and service_class == "MainService") or \
                (robot_class == "MaleRobot" and service_class == "SecondaryService"):
            return f"Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot.name} to {service.name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.find_service_by_name(service_name)
        robot = self.find_robot_in_service_by_name(service, robot_name)

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_service_by_name(service_name)
        [r.eating() for r in service.robots]

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.find_service_by_name(service_name)
        total_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def find_robot_by_name(self, name: str):
        robot = [r for r in self.robots if r.name == name][0]
        return robot

    def find_service_by_name(self, name: str):
        service = [s for s in self.services if s.name == name][0]
        return service

    @staticmethod
    def find_robot_in_service_by_name(service: BaseService, robot_name: str):
        try:
            robot = [r for r in service.robots if r.name == robot_name][0]
            return robot
        except IndexError:
            raise Exception("No such robot in this service!")
