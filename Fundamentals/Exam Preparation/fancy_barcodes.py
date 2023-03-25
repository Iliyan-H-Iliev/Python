import re

pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

n = int(input())

products = []

for _ in range(n):
    product = input()
    product_group = ""
    products.append(product)

    if re.match(pattern, product):
        prod = re.findall(pattern, product)
        item = str(prod[0])

        for char in item:
            if char.isdigit():
                product_group += char
        if product_group:
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")

    else:
        print("Invalid barcode")
