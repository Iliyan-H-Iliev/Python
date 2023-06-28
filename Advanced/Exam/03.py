def gather_credits(credits_1, *args):
    curses_list = []
    win_credits = 0
    result = ""

    for curse, credit in args:
        if curse not in curses_list and win_credits < credits_1:
            curses_list.append(curse)
            win_credits -= credit
        if abs(win_credits) >= credits_1:
            break

    if abs(win_credits) >= credits_1:
        result += f"Enrollment finished! Maximum credits: {abs(win_credits)}.\n"
        result += f"Courses: {', '.join(x for x in sorted(curses_list, key=lambda x: x))}"
    else:
        result += f"You need to enroll in more courses! You have to gather {credits_1 - abs(win_credits)} credits more."

    return result


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
