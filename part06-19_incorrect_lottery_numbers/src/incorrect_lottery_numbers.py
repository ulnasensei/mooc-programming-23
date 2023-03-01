def filter_incorrect():
    open("correct_numbers.csv", "w").close()
    with open("lottery_numbers.csv") as file:
        lines = [x.strip() for x in file.readlines()]
    with open("correct_numbers.csv", "a") as file:
        for line in lines:
            week, numbers = line.split(";")
            try:
                week_no = int(week.replace("week ", ""))

                numbers_list = [int(x) for x in numbers.split(",")]

                assert len(numbers_list) == 7

                for number in numbers_list:
                    assert 1 <= number <= 39

                assert len(set(numbers_list)) == 7

                file.write(line + "\n")
            except:
                pass
