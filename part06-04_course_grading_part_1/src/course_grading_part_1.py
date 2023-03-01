students_file = input("Students file: ")
exercises_file = input("Exercises file: ")

data = {}

with open(students_file, "r") as file:
    for line in file:
        line = line.strip()

        parts = line.split(";")

        if parts[0] == "id":
            continue

        student_id, first_name, last_name = parts

        data[student_id] = {}
        data[student_id]["first_name"] = first_name
        data[student_id]["last_name"] = last_name

with open(exercises_file, "r") as file:
    for line in file:
        line = line.strip()

        parts = line.split(";")

        if parts[0] == "id":
            continue

        student_id, exercises = parts[0], parts[1::]

        data[student_id]["exercises"] = [int(x) for x in exercises]


for student in data.values():
    print(
        f'{student.get("first_name")} {student.get("last_name")} {sum(student.get("exercises"))}'
    )
