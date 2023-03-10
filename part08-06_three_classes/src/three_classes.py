class Checklist:
    def __init__(self, header: str, entries: list) -> None:
        self.header: str = header
        self.entries: list = entries


class Customer:
    def __init__(self, id: str, balance: float, discount: int) -> None:
        self.id: str = id
        self.balance: float = balance
        self.discount: int = discount


class Cable:
    def __init__(
        self, model: str, length: float, max_speed: int, bidirectional: bool
    ) -> None:
        self.model: str = model
        self.length: float = length
        self.max_speed: int = max_speed
        self.bidirectional: bool = bidirectional
