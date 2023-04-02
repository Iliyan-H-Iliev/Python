import re

text = input()
total_cal = 0

pattern = r"(\||#)([A-Za-z\s]+)\1(\d\d\/\d\d\/\d\d)\1(\d+)\1"

products = re.findall(pattern, text)

for el in products:
    total_cal += int(el[3])

print(f"You have food to last you for: {total_cal // 2000} days!")
if products:
    for el in products:
        print(f"Item: {el[1]}, Best before: {el[2]}, Nutrition: {el[3]}")
