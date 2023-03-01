import csv
from datetime import timedelta


def cheaters() -> list:

    cheat_list = []
    start_times = {}
    with open("start_times.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            print(line)
            start_times[line[0]] = timedelta(
                hours=int(line[1].split(":")[0]), minutes=int(line[1].split(":")[1])
            )

    with open("submissions.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            name, task, points, time = line
            hh, mm = [int(x) for x in time.split(":")]
            submission_time = timedelta(hours=hh, minutes=mm)
            if (submission_time.seconds / 3600) - (
                start_times[name].seconds / 3600
            ) > 3:
                if name not in cheat_list:
                    cheat_list.append(name)
    return cheat_list
