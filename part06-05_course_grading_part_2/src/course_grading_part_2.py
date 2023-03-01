students_file = input("Students file: ")
exercises_file = input("Exercises file: ")
exam_points_file = input("Exam points file: ")


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
        data[student_id]["completed_exercise_points"] = (
            (sum(data[student_id]["exercises"]) * 100) / 40
        ) // 10

with open(exam_points_file, "r") as file:
    for line in file:
        line = line.strip()

        parts = line.split(";")

        if parts[0] == "id":
            continue

        student_id, exam_points = parts[0], parts[1::]

        data[student_id]["exam_points"] = sum([int(x) for x in exam_points])
        data[student_id]["total_points"] = (
            data[student_id]["completed_exercise_points"]
            + data[student_id]["exam_points"]
        )
        grade = data[student_id]["total_points"]
        if grade <= 14:
            data[student_id]["grade"] = 0
        elif grade <= 17:
            data[student_id]["grade"] = 1
        elif grade <= 20:
            data[student_id]["grade"] = 2
        elif grade <= 23:
            data[student_id]["grade"] = 3
        elif grade <= 27:
            data[student_id]["grade"] = 4
        else:
            data[student_id]["grade"] = 5

for student in data.values():
    print(
        f'{student.get("first_name")} {student.get("last_name")} {student.get("grade")}'
    )
