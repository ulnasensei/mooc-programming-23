def get_station_data(filename: str) -> dict:
    data = {}

    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()][1:]
    for line in lines:
        line_data = line.split(";")
        data[line_data[3]] = (float(line_data[0]), float(line_data[1]))

    return data


def distance(stations: dict, station1: str, station2: str) -> float:
    import math

    longitude1, latitude1 = stations.get(station1)
    longitude2, latitude2 = stations.get(station2)
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


def greatest_distance(stations: dict) -> tuple[str, str, float]:
    distances = {}

    station_names = list(stations.keys())

    for i in range(len(station_names)):
        for j in range( i + 1, len(station_names)):
            dist = distance(stations, station_names[i], station_names[j])
            distances[dist] = [station_names[i], station_names[j]]

    greatest = sorted(distances.keys())[-1]

    return (*distances[greatest], greatest)
