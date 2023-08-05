from project.software.software import Software


class ExpressSoftware(Software):
    SOFTWARE_TYPE = "Express"

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, ExpressSoftware.SOFTWARE_TYPE, capacity_consumption, memory_consumption * 2)

