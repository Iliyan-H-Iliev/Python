from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        res = f"{self.name} Secondary Service:\nRobots: "

        if self.robots:
            res += f"{' '.join([r.name for r in self.robots])}"
        else:
            res += "none"

        return res
