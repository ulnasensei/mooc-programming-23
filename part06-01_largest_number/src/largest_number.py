def largest() -> int:
    with open('numbers.txt', 'r') as text_file:
        largest = 0

        for line in text_file:
            num = int(line.replace('\n', ''))
            if num > largest:
                largest = num
        return largest
