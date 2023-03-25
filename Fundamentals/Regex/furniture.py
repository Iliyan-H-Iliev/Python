import re

pattern = r"(^|(?<=\s))>>(?P<mebels>[A-Z][A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<count>\d+)($|(?=\s))"

total_price = 0
all_furniture = []

while True:
    text = input()

    if text == "Purchase":
        break

    if re.match(pattern, text):
        result = re.finditer(pattern, text)
        for fur in result:
            furni = fur.groupdict()

            all_furniture.append(furni["mebels"])
            total_price += float(furni["price"]) * int(furni["count"])

print("Bought furniture:")
for el in all_furniture:
    print(el)
print(f"Total money spend: {total_price:.2f}")
