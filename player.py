class Player:

    # TODO: delete , and space after str in line 3
    def __init__(self, name: str, ) -> None:
        self.name = name
        # TODO: rename positon -> position
        self.positon = 0
    
    def set_position(self, position: int) -> None:
        self.position = position
    
    # TODO: rename from present -> current
    def get_present_position(self) -> int:
        return self.position