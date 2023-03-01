phone_book = {}

while True:
    command = int(input("1 search, 2 add, 3 quit: "))
    if command == 3:
        print("quitting...")
        break
    if command == 2:
        name = input("name: ")
        number = input("phone number: ")
        if name not in phone_book:
            phone_book[name] = []
        phone_book[name].append(number)
        print("ok!")
    elif command == 1:
        name = input("name: ")
        if name in phone_book:
            print("\n".join(phone_book[name]))
        else:
            print("no number")
