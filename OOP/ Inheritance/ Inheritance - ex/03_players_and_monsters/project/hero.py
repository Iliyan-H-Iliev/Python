class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __str__(self):
        return f"{self.username} of type {self.__class__.__qualname__} has level {self.level}"

