class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, sec_number):
        super().__init__(name)      # == Person.__init__(self, name, age)
        self.sec_number = sec_number
