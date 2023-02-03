def order_calculator(a, n):
    result = 0
    if a == "coffee":
        result = 1.5 * n
    elif a == "water":
        result = 1 * n
    elif a == "coke":
        result = 1.4 * n
    elif a == "snacks":
        result = 2 * n
    return result


product = input()
quantity = int(input())

print(f"{order_calculator(product, quantity):.2f}")
