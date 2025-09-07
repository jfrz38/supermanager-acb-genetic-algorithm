class Player:
    def __init__(self, team: str, name: str, position: str, value: int, price: int, work_permit: str) -> None:
        self.team = team
        self.name = name
        self.position = position
        self.value = value
        self.price = price
        self.work_permit = work_permit
    
    def __repr__(self) -> str:
        return '{} {} ({}) -> {}€'.format(self.position, self.name, self.team, self.price)
