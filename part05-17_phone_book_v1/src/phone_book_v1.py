phone_book = {}

while True:
    command = int(input("1 search, 2 add, 3 quit: "))
    if command == 3:
        print("quitting...")
        break
    if command == 2:
        name = input("name: ")
        number = input("phone number: ")
        phone_book[name] = number
        print("ok!")
    elif command == 1:
        name = input("name: ")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("no number")
