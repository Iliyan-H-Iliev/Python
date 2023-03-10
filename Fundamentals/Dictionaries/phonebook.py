phonebook = {}

contact = input()

while "-" in contact:
    name, phone_number = contact.split("-")
    phonebook[name] = phone_number
    contact = input()

search = int(contact)

for _ in range(search):
    search_name = input()

    if phonebook.get(search_name):
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
