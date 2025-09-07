class Team:
    def __init__(self, players) -> None:
        self.players = players

    def count(self, player):
        return self.players.count(player)

    def index(self, player):
        return self.players.index(player)

    def __len__(self):
        return len(self.players)

    def __iter__(self):
        return iter(self.players)

    def __getitem__(self, item):
        return self.players[item]

    def __setitem__(self, key, value):
        self.players[key] = value

    def __repr__(self):
        str = ""
        for p in self.players:
            str+= '{}: {} ({}) -> ${}'.format(p.position, p.name, p.team, p.price) + " ; "
        return str
