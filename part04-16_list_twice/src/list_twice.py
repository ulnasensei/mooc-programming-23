mylist = []

while True:
    number = int(input())
    if number == 0:
        print("Bye!")
        break
    mylist.append(number)
    print(f"The list now: {mylist}")
    print(f"The list in order: {sorted(mylist)}")
