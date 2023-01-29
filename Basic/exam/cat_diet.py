percent_fats = int(input())
percent_proteins = int(input())
percent_carbs = int(input())
total_calories = int(input())
percent_water = int(input())

fat_calories = 9
protein_calories = 4
carb_calories = 4

total_fat = (total_calories * (percent_fats / 100)) / fat_calories
total_protein = (total_calories * (percent_proteins / 100)) / protein_calories
total_carb = (total_calories * (percent_carbs / 100)) / carb_calories

calories = (total_calories / (total_fat + total_protein + total_carb)) * ((100 - percent_water) / 100)

print(f"{calories:.4f}")
