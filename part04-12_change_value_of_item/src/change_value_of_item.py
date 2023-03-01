a_list = [1, 2, 3, 4, 5]

while True:
    index = int(input())
    if index == -1:
        break
    new_item = int(input())
    a_list[index] = new_item
    print(a_list)
