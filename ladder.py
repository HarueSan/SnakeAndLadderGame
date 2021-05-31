from error import *


class Ladder:

    def __init__(self, start: int, end: int) -> None:
        self.validate(start, end)
        self.start = start
        self.end = end

    # debug
    def __repr__(self) -> None:
        return f"start:<{self.start}, end:<{self.end}>"

    def validate(self, start: int, end: int) -> None:
        if start == end:
            raise PositionLadderError("Start ladder equal end ladder")

        elif start > end:
            raise PositionLadderError("Start ladder more than end ladder")

        elif start == 1 or end == 1:
            raise PositionLadderError("Start ladder or end ladder equal start point ")

        elif start < 1 or end < 1:
            raise InvalidInputError("Negative number or zero")
