class Clock:
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self) -> str:
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}"

    def tick(self):
        if self.second == 59:
            self.second = 0
            if self.minute == 59:
                self.minute = 0
                if self.hour == 23:
                    self.hour = 0
                else:
                    self.hour += 1
            else:
                self.minute += 1
        else:
            self.second += 1

    def set(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute
        self.second = 0
