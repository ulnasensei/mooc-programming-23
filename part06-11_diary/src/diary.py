while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    option = int(input("function: "))

    if option == 0:
        print("Bye now!")
        break
    if option == 1:
        entry = input("entry: ")
        with open("diary.txt", "a") as diary:
            diary.write(entry + "\n")
        print("Diary saved")
    if option == 2:
        print("Entries:")
        with open("diary.txt") as diary:
            print(diary.read())
