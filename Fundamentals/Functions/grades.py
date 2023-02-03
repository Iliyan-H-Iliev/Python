def grades(a):
    if 2 <= a <= 2.99:
        return "Fail"
    elif 3 <= a <= 3.49:
        return "Poor"
    elif 3.50 <= a <= 4.49:
        return "Good"
    elif 4.50 <= a <= 5.49:
        return "Very Good"
    elif 5.50 <= a <= 6:
        return "Excellent"


grade = float(input())

print(grades(grade))
