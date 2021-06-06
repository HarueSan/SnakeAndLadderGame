from snake_error import *


class Snake:
    
    def __init__(self, head: int, tail: int) -> None:
        self.validate(head, tail)
        self.head = head
        self.tail = tail
    
    # debug
    def __repr__(self) -> str:
        return f"head:<{self.head}, tail:<{self.tail}>"

    def validate_head_less_than_tail(self, head: int, tail: int) -> None:
        if head < tail:
            raise HeadSnakeLessThanTailSnake(self)

    def validate_head_equal_tail(self, head: int, tail: int) -> None:
        if head == tail:
            raise HeadSnakeEqualTailSnake(self)

    def validate(self, head: int, tail: int) -> None:
        self.validate_head_less_than_tail(head, tail)
        self.validate_head_equal_tail(head, tail)
