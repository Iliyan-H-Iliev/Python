lessons_and_exercises = input().split(", ")


while True:
    command = input()

    if command == "course start":
        break


    split_command = command.split(":")
    lesson_command = command[0]
    lesson_title = split_command[1]

    if lesson_command == "Add":
        if lesson_title not in lessons_and_exercises:
            lessons_and_exercises.append(lesson_title)

    elif lesson_command == "Insert":
        if lesson_title not in lessons_and_exercises:
            lessons_and_exercises.insert(int(split_command[2]), lesson_title)
        pass
    elif lesson_command == "Remove":
        if lesson_title not in lessons_and_exercises:
            lessons_and_exercises.remove(lesson_title)
    elif lesson_command == "Swap":
        if lesson_title in lessons_and_exercises and split_command[2] in lessons_and_exercises:
            pass
        lessons_and_exercises.index(lesson_title), lessons_and_exercises.index(split_command[2]) = \
            lessons_and_exercises.index(split_command[2]), lessons_and_exercises.index(lesson_title)
    elif lesson_command == "Exercise":
        pass

    # •	"Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
    # •	"Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
    # •	"Remove:{lessonTitle}" - remove the lesson, if it exists.
    # •	"Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
    # •	"Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index, if the lesson exists and there is no exercise already, in the following format "{lessonTitle}-Exercise". If the lesson doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.
    # Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises, if there are any following the lessons.