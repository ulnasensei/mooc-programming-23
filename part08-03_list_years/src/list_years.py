from datetime import date


def list_years(dates: list[date]) -> list[int]:
    return sorted([x.year for x in dates])
