class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"

        if self.__budget >= price and self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__qualname__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__qualname__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):

        total_payment = sum(worker.salary for worker in self.workers)

        if self.__budget < total_payment:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_payment
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_payment = sum(animal.money_for_care for animal in self.animals)

        if self.__budget < total_payment:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_payment
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__qualname__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__qualname__ == "Tiger":
                tigers.append(animal)
            else:
                cheetahs.append(animal)
        result = f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n"
        result += "\n".join(lion.__repr__() for lion in lions)
        result += f"\n----- {len(tigers)} Tigers:\n"
        result += "\n".join(tiger.__repr__() for tiger in tigers)
        result += f"\n----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join(cheetah.__repr__() for cheetah in cheetahs)
        return result

    def workers_status(self):
        keepers = []
        caretaker = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__qualname__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__qualname__ == "Vet":
                vets.append(worker)
            else:
                caretaker.append(worker)

        result = f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n"
        result += "\n".join(k.__repr__() for k in keepers)
        result += f"\n----- {len(caretaker)} Caretakers:\n"
        result += "\n".join(c.__repr__() for c in caretaker)
        result += f"\n----- {len(vets)} Vets:\n"
        result += "\n".join(v.__repr__() for v in vets)

        return result
