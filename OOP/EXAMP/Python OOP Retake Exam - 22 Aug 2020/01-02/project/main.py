from project.rooms.alone_old import AloneOld
from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren
from people.child import Child
from everland import Everland

everland = Everland()

young_couple = YoungCouple("Johnsons", 150, 205)
old = AloneOld("asdf", 250)

child1 = Child(5, 1)
child2 = Child(3, 2)
young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)


everland.add_room(young_couple)

everland.add_room(young_couple_with_children)
everland.add_room(old)

print(young_couple_with_children.appliances)

print(everland.get_monthly_consumptions())
print(everland.pay())
print(everland.status())


