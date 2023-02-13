lessons_and_exercises = input().split(", ")

while True:
    command = input()

    if command == "course start":
        break

    split_command = command.split(":")
    lesson_command = split_command[0]
    lesson_title = split_command[1]

    if lesson_command == "Add":
        if lesson_title not in lessons_and_exercises:
            lessons_and_exercises.append(lesson_title)

    elif lesson_command == "Insert":
        index = int(split_command[2])
        if lesson_title not in lessons_and_exercises:
            lessons_and_exercises.insert(index, lesson_title)

    elif lesson_command == "Remove":
        if lesson_title in lessons_and_exercises:
            lessons_and_exercises.remove(lesson_title)
        if f"{lesson_title}-Exercise" in lessons_and_exercises:
            lessons_and_exercises.remove(f"{lesson_title}-Exercise")

    elif lesson_command == "Swap":
        second_lesson_title = split_command[2]

        if lesson_title in lessons_and_exercises and second_lesson_title in lessons_and_exercises:
            first_lesson_index = lessons_and_exercises.index(lesson_title)
            second_lesson_index = lessons_and_exercises.index(second_lesson_title)

            lessons_and_exercises[first_lesson_index], lessons_and_exercises[second_lesson_index] = \
                lessons_and_exercises[second_lesson_index], lessons_and_exercises[first_lesson_index]

            if f"{lesson_title}-Exercise" in lessons_and_exercises:
                lessons_and_exercises.remove(f"{lesson_title}-Exercise")
                lessons_and_exercises.insert(second_lesson_index + 1, f"{lesson_title}-Exercise")

            if f"{second_lesson_title}-Exercise" in lessons_and_exercises:
                lessons_and_exercises.remove(f"{second_lesson_title}-Exercise")
                lessons_and_exercises.insert(first_lesson_index + 1, f"{second_lesson_title}-Exercise")

    elif lesson_command == "Exercise":
        if lesson_title in lessons_and_exercises and f"{lesson_title}-Exercise" not in lessons_and_exercises:
            lesson_index = lessons_and_exercises.index(lesson_title)
            lessons_and_exercises.insert(lesson_index + 1, f"{lesson_title}-Exercise")
        elif lesson_title not in lessons_and_exercises:
            lessons_and_exercises.append(lesson_title)
            lessons_and_exercises.append(f"{lesson_title}-Exercise")

for i in range(len(lessons_and_exercises)):
    print(f"{i + 1}.{lessons_and_exercises[i]}")
