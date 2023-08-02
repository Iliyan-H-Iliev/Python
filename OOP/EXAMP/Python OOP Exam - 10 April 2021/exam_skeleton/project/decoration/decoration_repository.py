from typing import List

from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:

    def __init__(self):
        self.decorations: List[BaseDecoration] = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration not in self.decorations:
            return False

        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        decorations = [d for d in self.decorations if d.__class__.__name__ == decoration_type]

        if not decorations:
            return "None"

        return decorations[0]