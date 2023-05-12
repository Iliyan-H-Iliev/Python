guest = set()

for _ in range(int(input())):
    guest.add(input())

while True:
    name = input()

    if name == "END":
        break
    if name in guest:
        guest.remove(name)

print(len(guest))
for el in sorted(guest):
    print(el)
