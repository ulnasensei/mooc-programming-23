import csv
from datetime import timedelta


def final_points() -> dict:
    submissions = {}

    with open("start_times.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            name, time = line
            hh, mm = [int(x) for x in time.split(":")]
            submissions[name] = {
                "start": timedelta(hours=hh, minutes=mm).seconds / 3600,
                "points": [0 for x in range(8)],
            }

    with open("submissions.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            name, task, points, time = line
            hh, mm = [int(x) for x in time.split(":")]
            task_submit = timedelta(hours=hh, minutes=mm).seconds / 3600

            if task_submit - submissions[name]["start"] > 3:
                continue

            if int(points) > submissions[name]["points"][int(task) - 1]:
                submissions[name]["points"][int(task) - 1] = int(points)

    return {key: sum(value["points"]) for key, value in submissions.items()}
