def find_movies(database: list, search_term: str) -> list:
    result = []

    for movie in database:
        if search_term.lower() in movie["name"].lower():
            result.append(movie)
    return result
