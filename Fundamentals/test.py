import re

pattern = r'([#|$|%|*|&])(?P<name>[A-Za-z]+)\1=(?P<num>\d+)!!(?P<code>[\w\W]+)'
password = ''

while True:
    text = input()

    if re.match(pattern, text):
        valid_text = re.finditer(pattern, text)
        for information in valid_text:
            geocode = information.group('name')
            number = int(information.group('num'))
            encrypted = information.group('code')
            if number == len(encrypted):
                for i in encrypted:
                    value = ord(i) + int(number)
                    char = chr(value)
                    password += char
                print(password)
        break
    else:
        print("Nothing found!")