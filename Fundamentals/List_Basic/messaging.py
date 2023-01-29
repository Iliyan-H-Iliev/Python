number_list = list(input().split())
original_text_list = [x for x in input()]
secret_messaging = []

for el in number_list:
    massaging_index = sum([int(x) for x in el])

    if massaging_index >= len(original_text_list):
        while massaging_index >= len(original_text_list):
            massaging_index -= len(original_text_list)

    secret_messaging.append(original_text_list[massaging_index])
    original_text_list.pop(massaging_index)

for i in secret_messaging:
    print(i, end="")
