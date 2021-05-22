class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.position = 0
    
    def set_position(self, position: int) -> None:
        self.position = position
  