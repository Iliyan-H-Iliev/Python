number_bottles = int(input()) * 750

detergent_used = 0
clean_pots = 0
plates_clean = 0
total_detergent = 0
is_detergent = False

while total_detergent <= number_bottles and is_detergent == False:

    for i in range(1, 3 + 1):
        dishes_number = input()

        if dishes_number == "End":
            is_detergent = True
            break

        if i < 3:
            plates_clean += int(dishes_number)
            detergent_used = int(dishes_number) * 5
            total_detergent += detergent_used
        else:
            clean_pots += int(dishes_number)
            detergent_used = int(dishes_number) * 15
            total_detergent += detergent_used

if is_detergent:
    print("Detergent was enough!")
    print(f"{plates_clean} dishes and {clean_pots} pots were washed.")
    print(f"Leftover detergent {number_bottles - total_detergent} ml.")
else:
    print(f"Not enough detergent, {total_detergent - number_bottles} ml. more necessary!")
