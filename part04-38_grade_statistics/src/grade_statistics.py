def calculate_grade(exam_points: int, exercise_points: int) -> tuple[int, bool]:
    total_points = exam_points + (exercise_points // 10)
    if exam_points < 10 or total_points <= 14:
        return (0, False)
    if total_points <= 17:
        return (1, True)
    if total_points <= 20:
        return (2, True)
    if total_points <= 23:
        return (3, True)
    if total_points <= 27:
        return (4, True)
    return (5, True)


def print_stats(
    total_points: int, points_count: int, passing: int, grades: list
) -> None:

    average = total_points / points_count
    pass_percentage = (100 * passing) / points_count

    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f'{i}: {"*" * grades[i]}')


points_total = 0
count_of_points = 0
passing = 0
grades = [0, 0, 0, 0, 0, 0]

while True:
    points_input = input()
    if len(points_input) == 0:
        print_stats(points_total, count_of_points, passing, grades)
        break
    exam_points, exercise_points = [int(point) for point in points_input.split()]
    count_of_points += 1
    points_total += exam_points + (exercise_points // 10)
    grade, pass_status = calculate_grade(exam_points, exercise_points)
    grades[grade] += 1
    if pass_status:
        passing += 1
