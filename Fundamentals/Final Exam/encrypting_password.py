import re

pattern = r"(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1"
n = int(input())

for _ in range(n):
    password = input()

    if not re.match(pattern, password):
        print("Try another password!")
    else:
        result = re.findall(pattern, password)
        encrypted_password = f"{result[0][1]}{result[0][2]}{result[0][3]}{result[0][4]}"
        print(f"Password: {encrypted_password}")
