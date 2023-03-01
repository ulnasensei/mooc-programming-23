def remove_smallest(numbers: list):
    smallest = numbers[0]
    for item in numbers:
        if item < smallest:
            smallest = item
    numbers.remove(smallest)
