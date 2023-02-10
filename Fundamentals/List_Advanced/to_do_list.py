def priority(importance):
    importance_notes = importance.split("-")
    prior = int(importance_notes[0]) - 1
    note_1 = importance_notes[1]
    ready_list.pop(prior)
    ready_list.insert(prior, note_1)


ready_list = [0] * 10

while True:
    notes = input()

    if notes == "End":
        break

    priority(notes)

print(list(el for el in ready_list if el != 0))
