exam_results = {}
count = {}

while True:

    line = input()
    if line == "exam finished":
        break

    if "banned" in line:
        args = line.split("-")
        username = args[0]
        for k, v in exam_results.items():
            if username in v:
                exam_results[k].pop(username)

    else:
        username, language, points = line.split("-")
        points = int(points)

        if language in exam_results:
            count[language] += 1
            if username in exam_results[language]:
                if exam_results[language][username] < points:
                    exam_results[language][username] = points
            else:
                exam_results[language][username] = points

        else:
            exam_results[language] = {username: points}
            count[language] = 1

print("Results:")

for v in exam_results.values():
    for name, point in v.items():
        print(f"{name} | {point}")

print("Submissions:")

for lang, c in count.items():
    print(f"{lang} - {c}")
