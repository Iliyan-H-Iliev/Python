def forecast(*args):
    result = ""
    whether_by_location = {
                "Sunny": [],
                "Cloudy": [],
                "Rainy": [],

    }
    for city, weather in args:
        whether_by_location[weather].append(city)

    for weather, cities in whether_by_location.items():
        for city in sorted(cities, key=lambda x: x):
            result += f"{city} - {weather}\n"

    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
