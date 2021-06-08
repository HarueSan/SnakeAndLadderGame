class Player:

    def __init__(self, player_name) -> None:
        self.position = 0
        self.name = player_name

    def __repr__(self) -> None:
        return f"name:<{self.name}>"
