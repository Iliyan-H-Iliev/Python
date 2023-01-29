book_pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

daily_pages = book_pages // days_per_book
hours_per_day = daily_pages // pages_per_hour

print(hours_per_day)
