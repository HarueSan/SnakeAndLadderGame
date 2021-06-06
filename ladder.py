from ladder_error import *


class Ladder:

    def __init__(self, start: int, end: int) -> None:
        self.validate(start, end)
        self.start = start
        self.end = end

    # debug
    def __repr__(self) -> str:
        return f"start:<{self.start}, end:<{self.end}>"

    def validate_start_ladder_equal_end_ladder(self, start, end) -> None:
        if start == end:
            raise StartLadderEqualEndLadder(self)

    def validate_start_ladder_over_end_ladder(self, start, end) -> None:
        if start > end:
            raise StartLadderOverEndLadder(self)

    def validate(self, start: int, end: int) -> None:
        self.validate_start_ladder_equal_end_ladder(start, end)
        self.validate_start_ladder_over_end_ladder(start, end)
