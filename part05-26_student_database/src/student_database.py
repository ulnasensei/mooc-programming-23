def add_student(students: dict, name: str):
    students[name] = {}


def print_student(students: dict, query: str):
    student: dict = students.get(query)
    if student is None:
        print(f"{query}: no such person in the database")
        return
    print(f"{query}:")
    if len(student) == 0:
        print(" no completed courses")
        return
    average_grade = sum(student.values()) / len(student)
    print(f" {len(student)} completed courses:")
    for key, value in student.items():
        print(f"  {key} {value}")
    print(f" average grade {average_grade}")


def add_course(students: dict, name: str, course: tuple):
    courses: dict = students.get(name)
    course_name, grade = course
    if len(courses) == 0 and grade != 0:
        courses[course_name] = grade
    else:
        if (
            course_name in courses.keys() and grade > courses[course_name]
        ) or (course_name not in courses.keys() and grade != 0):
            courses[course_name] = grade
    students[name] = courses


def summary(students: dict):
    most_courses_count = 0
    most_courses_name = ""

    for key, value in students.items():
        course_count = len(value)
        if course_count > most_courses_count:
            most_courses_count = course_count
            most_courses_name = key

    best_average_grade = 0
    best_average_name = ""

    for key, value in students.items():
        average = sum(value.values()) / len(value)
        if average > best_average_grade:
            best_average_grade = average
            best_average_name = key

    print(f"students {len(students)}")
    print(f"most courses completed {most_courses_count} {most_courses_name}")
    print(f"best average grade {best_average_grade} {best_average_name}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Emily")
    print_student(students, "Peter")
    print_student(students, "Emily")
    print_student(students, "Andy")
    add_course(students, "Peter", ("Introduction to Programming", 5))
