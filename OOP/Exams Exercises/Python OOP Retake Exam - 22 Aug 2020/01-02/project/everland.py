from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0

        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        res = []
        for room in self.rooms:
            room_monthly_consumptions = room.room_cost + room.expenses

            if room.budget >= room_monthly_consumptions:
                room.budget -= room_monthly_consumptions
                res.append(f"{room.family_name} paid {room_monthly_consumptions:.2f}$ "
                           f"and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                res.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return "\n".join(res)

    def status(self):
        res = [f"Total population: {sum(r.members_count for r in self.rooms)}"]

        for room in self.rooms:
            room_app = sum(a.cost for a in room.appliances) * 30
            res.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, "
                       f"Expenses: {room.expenses:.2f}$")
            if room.children:
                for i in range(len(room.children)):
                    res.append(f"--- Child {i + 1} monthly cost: {(room.children[i].cost * 30):.2f}$")

            res.append(f"--- Appliances monthly cost: {room_app:.2f}$")

        return "\n".join(res)






