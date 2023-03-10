# DO NOT CHANGE CLASS Book!
# Write your solution after the class!


class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year


# -----------------------------
# Write your solution here
# -----------------------------


def older_book(book1: Book, book2: Book):
    diff = book1.year - book2.year
    if diff < 0:
        print(f"{book1.name} is older, it was published in {book1.year}")
    elif diff > 0:
        print(f"{book2.name} is older, it was published in {book2.year}")
    else:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")
