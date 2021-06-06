class StartLadderEqualEndLadder(Exception):

    def __init__(self, ladder: "Ladder") -> None:
        self.ladder = ladder

    def __str__(self) -> str:
        return f"{self.ladder.play}  equal {self.ladder.end}"


class StartLadderOverEndLadder(Exception):

    def __init__(self, ladder: "Ladder") -> None:
        self.ladder = ladder

    def __str__(self) -> str:
        return f"{self.ladder.play}  more than {self.ladder.end}"


class StartLadderOrEndLadderEqualStartPoint(Exception):

    def __init__(self, ladder: "Ladder") -> None:
        self.ladder = ladder

    def __str__(self) -> str:
        return f"{self.ladder.play} or {self.ladder.end} equal start point"


class LadderSyntaxInputError(Exception):

    def __init__(self, ladder: "Ladder") -> None:
        self.ladder = ladder

    def __str__(self) -> str:
        return f"{self.ladder.play} or {self.ladder.end} is Negative number or zero"
