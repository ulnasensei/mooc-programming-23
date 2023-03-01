mylist = []

while True:
    print(f"The list is now {mylist}")
    choice = input()
    if choice.lower() == "d":
        mylist.append(1 if len(mylist) == 0 else mylist[-1] + 1)
    elif choice.lower() == "r":
        mylist.pop()
    elif choice.lower() == "x":
        print("Bye!")
        break
