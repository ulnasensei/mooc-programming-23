def filter_solutions():
    with open("solutions.csv") as file:
        data = [x.strip() for x in file.readlines()]

    # Cleaning the result files
    open("correct.csv", "w").close()
    open("incorrect.csv", "w").close()

    for line in data:
        equasion, result = line.split(";")[1:]
        if "-" in equasion:
            a, b = (int(x) for x in equasion.split("-"))
            if a - b == int(result):
                with open("correct.csv", "a") as file:
                    file.write(line + "\n")
            else:
                with open("incorrect.csv", "a") as file:
                    file.write(line + "\n")
            continue
        if "+" in equasion:
            a, b = (int(x) for x in equasion.split("+"))
            if a + b == int(result):
                with open("correct.csv", "a") as file:
                    file.write(line + "\n")
            else:
                with open("incorrect.csv", "a") as file:
                    file.write(line + "\n")
