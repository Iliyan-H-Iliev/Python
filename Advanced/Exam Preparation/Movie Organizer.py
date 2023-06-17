def movie_organizer(*args):
    result = ""
    sort_movies = {}
    for name, genre in args:
        if genre not in sort_movies:
            sort_movies[genre] = []
        sort_movies[genre].append(name)

    for genre, movies in sorted(sort_movies.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{genre} - {len(movies)}\n"
        for movie in sorted(movies, key=lambda x: x):
            result += f"* {movie}\n"

    return result


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

print()
print()

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
