import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


def create_pet(name: str, species: str):
    pet = Pet.objects.create(
        name=name,
        species=species, )
    return f"{pet.name} is a very cute {pet.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )
    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all().order_by("-id")

    return '\n'.join(f"{str(l.name)} has a population of {str(l.population)}!" for l in locations)


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        discount = float(car.price) * sum([int(x) for x in str(car.year)]) / 100
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values("model", "price_with_discount")


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    tasks = Task.objects.filter(is_finished=False)

    return "\n".join(f"Task - {t.title} needs to be done until {t.due_date}!" for t in tasks)


def complete_odd_tasks():
    tasks = Task.objects.filter(id__iregex=r"^\d*[13579]$")
    for t in tasks:
        t.is_finished = True
        t.save()


def encode_and_replace(text: str, task_title: str):

    encoding_text = "".join(chr(ord(x) - 3) for x in text)
    Task.objects.filter(title=task_title).update(description=encoding_text)


def get_deluxe_rooms():
    rooms = HotelRoom.objects.filter(id__iregex=r"^\d*[02468]$", room_type="Deluxe")

    return "\n".join(f"Deluxe room with number "
                     f"{r.room_number} costs {r.price_per_night}$ per night!" for r in rooms)


def increase_room_capacity():
    increase_number = None
    rooms = HotelRoom.objects.all().order_by("id")

    for r in rooms:
        if not r.is_reserved:
            continue

        if increase_number:
            r.capacity += increase_number
        else:
            r.capacity += r.id

        increase_number = r.capacity
        r.save()


def reserve_first_room():
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room():
    HotelRoom.objects.last().delete()