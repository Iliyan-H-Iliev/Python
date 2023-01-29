student_tickets = 0
standard_tickets = 0
kids_tickets = 0
total_tickets = 0

while True:
    movie_name = input()

    if movie_name == "Finish":
        break

    capacity = int(input())
    ticket_count = 0

    while ticket_count < capacity:
        ticket_type = input()

        if ticket_type == "End":
            break

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        else:
            kids_tickets += 1

        total_tickets += 1
        ticket_count += 1

    print(f"{movie_name} - {(ticket_count / capacity) * 100:.2f}% full.")
print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kids_tickets / total_tickets) * 100:.2f}% kids tickets.")
