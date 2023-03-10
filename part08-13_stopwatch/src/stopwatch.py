# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes = 0
            else:
                self.minutes += 1
        else:
            self.seconds += 1

    def __str__(self) -> str:
        return f"{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"
