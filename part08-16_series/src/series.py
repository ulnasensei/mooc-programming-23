class Series:
    def __init__(self, title: str, seasons: int, genres: list) -> None:
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rates = []
        self.rating_avg = 0

    def __str__(self) -> str:
        return f'{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{"no ratings" if len(self.rates) == 0 else f"{len(self.rates)} ratings, average {self.rating_avg:.1f} points"}'

    def rate(self, rating):
        self.rates.append(rating)
        self.rating_avg = sum(self.rates) / len(self.rates)


def minimum_grade(rating: float, series_list: list) -> list:
    return [series for series in series_list if series.rating_avg > rating]


def includes_genre(genre: str, series_list: list) -> list:
    return [series for series in series_list if genre in series.genres]
