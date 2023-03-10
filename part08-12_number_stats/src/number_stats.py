# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if self.count_numbers() == 0:
            return 0
        return self.get_sum() / self.count_numbers()


stats = NumberStats()
evens = NumberStats()
odds = NumberStats()

while True:
    number = int(input("number: "))

    if number == -1:
        break
    stats.add_number(number)
    if number % 2 == 1:
        odds.add_number(number)
    else:
        evens.add_number(number)

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {evens.get_sum()}")
print(f"Sum of odd numbers: {odds.get_sum()}")
