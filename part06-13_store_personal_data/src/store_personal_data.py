def store_personal_data(person: tuple):
    with open("people.csv", "a") as file:
        file.write(";".join((str(x) for x in person)) + "\n")
