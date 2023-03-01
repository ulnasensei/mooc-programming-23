students_file = input("Students file: ")
exercises_file = input("Exercises file: ")
exam_points_file = input("Exam points file: ")
course_info_file = input("Course info file: ")

data = {}

with open(students_file, "r") as file:
    for line in file:
        line = line.strip()

        parts = line.split(";")

        if parts[0] == "id":
            continue

        student_id, first_name, last_name = parts

        data[student_id] = {}
        data[student_id]["name"] = first_name + " " + last_name

with open(exercises_file, "r") as file:
    for line in file:
        line = line.strip()

        parts = line.split(";")

        if parts[0] == "id":
            continue

        student_id, exercises = parts[0], parts[1::]

        data[student_id]["exercises"] = [int(x) for x in exercises]
        data[student_id]["exercise_points"] = int(
            ((sum(data[student_id]["exercises"]) * 100) / 40) // 10
        )

with open(exam_points_file, "r") as file:
    for line in file:
        line = line.strip()

        parts = line.split(";")

        if parts[0] == "id":
            continue

        student_id, exam_points = parts[0], parts[1::]

        data[student_id]["exam_points"] = sum([int(x) for x in exam_points])
        data[student_id]["total_points"] = (
            data[student_id]["exercise_points"] + data[student_id]["exam_points"]
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

with open(course_info_file) as file:
    course_name, credits = (x.split(":")[1].strip() for x in file.readlines())
    open("results.txt", "w").close()
    result = open("results.txt", "a")
    result.write(f"{course_name}, {credits} credits\n")
    result.write("======================================\n")

    result.write(
        f"{'name':30}{'exec_nbr':10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}\n"
    )
    for student in data.values():
        result.write(
            f"{student.get('name'):30}{sum(student.get('exercises')):<10}{student.get('exercise_points'):<10}{student.get('exam_points'):<10}{student.get('total_points'):<10}{student.get('grade'):<10}\n"
        )
    result.close()

open("results.csv", "w").close()
result_csv = open("results.csv", "a")

for student_id, info in data.items():
    result_csv.write(f"{student_id};{info.get('name')};{info.get('grade')}\n")
result_csv.close()
