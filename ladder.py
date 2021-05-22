class Ladder:

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __repr__(self):
        return f"start <{self.start}> end <{self.end}>"
        