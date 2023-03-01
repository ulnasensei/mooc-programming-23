while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    option = input("Option: ")
    if option == "3":
        print("Bye!")
        break

    if option == "2":
        search = input("Search: ")
        with open("dictionary.txt") as file:
            words = [x.strip() for x in file.readlines()]
        for couple in words:
            finnish, english = couple.split(";")
            if search.lower() in finnish.lower() or search.lower() in english.lower():
                print(f"{finnish} - {english}")
        continue

    if option == "1":
        finnish = input("Finnish: ")
        english = input("English: ")
        with open("dictionary.txt", "a") as file:
            file.write(f"{finnish};{english}\n")
            print("Dictionary entry added")
