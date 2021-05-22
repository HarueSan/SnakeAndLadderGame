class Snake:
    
    def __init__(self, head: int, tail: int) -> None:
        self.head = head
        self.tail = tail

    def __repr__(self):
        return f"head <{self.head}> end <{self.tail}>"
