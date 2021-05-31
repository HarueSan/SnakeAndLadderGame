from error import *


class Snake:
    
    def __init__(self, head: int, tail: int) -> None:
        self.validate_snake(head, tail)
        self.head = head
        self.tail = tail
    
    # debug
    def __repr__(self):
        return f"head:<{self.head}, tail:<{self.tail}>"

    def validate_snake(self, head: int, tail: int) -> None:
        if head < tail:
            raise PositionSnakeError("Head snake less than tail snake")

        elif head == tail:
            raise PositionSnakeError("Head snake equal tail snake")

        elif head == 1 or tail == 1:
            raise PositionSnakeError("Head snake or tail snake equal start point")

        elif head < 1 or tail < 1:
            raise InvalidInputError("Negative number or zero")
