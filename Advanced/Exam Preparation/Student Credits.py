def students_credits(*args):
    result = ""
    total_credits = 0
    courses = {}
    for el in args:
        elements = [int(x) if x.isdigit() else x for x in el.split("-")]
        course_name, credit, max_point, points = elements
        courses[course_name] = credit / max_point * points
        total_credits += courses[course_name]

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

    for course, credit in sorted(courses.items(), key=lambda x: -x[1]):
        result += f"{course} - {credit:.1f}\n"

    return result


print(students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)



print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
