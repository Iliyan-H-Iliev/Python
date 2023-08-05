from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self. vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{user.first_name} {user.last_name} was successfully " \
               f"registered under DLN-{user.driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type not in ["CargoVan", "PassengerCar"]:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        if vehicle_type == "CargoVan":
            vehicle = CargoVan(brand, model, license_plate_number)
        else:
            vehicle = PassengerCar(brand, model, license_plate_number)

        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):

        for route in self.routes:

            if route.start_point == start_point and route.end_point == end_point:

                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."

                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."

                else:
                    route.is_locked = True

        route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):

        user = [user for user in self.users if user.driving_license_number == driving_license_number][0]
        vehicle = [vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number][0]
        route = [route for route in self.routes if route.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            user.decrease_rating()
            vehicle.change_status()
        else:
            user.increase_rating()

        return str(vehicle)

    def find_damaged_vehicles(self, count: int):
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        damaged_vehicles.sort(key=lambda x: (x.brand, x.model))

        if len(damaged_vehicles) > count:
            damaged_vehicles = damaged_vehicles[:count]

        return damaged_vehicles, len(damaged_vehicles)

    def repair_vehicles(self, count: int):
        damaged_vehicles, count = self.find_damaged_vehicles(count)

        for vehicle in damaged_vehicles:
            vehicle.recharge()
            vehicle.change_status()

        return f"{count} vehicles were successfully repaired!"

    def users_report(self):
        res = "*** E-Drive-Rent ***\n"
        res += '\n'.join([str(user) for user in sorted(self.users, key=lambda x: (-x.rating))])
        return res

