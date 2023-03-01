import urllib.request
import json
from math import floor


def retrieve_all() -> list:
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    data = json.loads(urllib.request.urlopen(url).read())
    data = list(filter(lambda x: x["enabled"], data))
    result = [(x["fullName"], x["name"], x["year"], sum(x["exercises"])) for x in data]
    return result


def retrieve_course(course_name: str) -> dict:
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    data: dict = json.loads(urllib.request.urlopen(url).read())
    students = sorted(data.values(), key=lambda x: x["students"], reverse=True)[0][
        "students"
    ]
    hours = sum([x["hour_total"] for x in data.values()])
    hours_average = floor(hours / students)
    exercises = sum([x["exercise_total"] for x in data.values()])
    exercises_average = floor(exercises / students)
    return {
        "weeks": len(data),
        "students": students,
        "hours": hours,
        "hours_average": hours_average,
        "exercises": exercises,
        "exercises_average": exercises_average,
    }
