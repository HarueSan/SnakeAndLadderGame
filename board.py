from typing import List, Optional
from ladder import Ladder
from snake import Snake
from player import Player
from board_error import *
from snake_error import *


class Board:

    def __init__(self, start_point: int, board_size: int, finish_line: int, ladders: List[Ladder], snakes: List[Snake]) -> None:
        self.start_point = start_point
        self.size = board_size
        self.finish_line = finish_line
        self.ladders: List[Ladder] = []
        self.snakes: List[Snake] = []

        # TODO: รอคุยกับพี่จีนส์
        for snake in snakes:
            try:
                self.add_snake(snake)

            except BoardAddSnakeError:
                pass

        for ladder in ladders:
            try:
                self.add_ladder(ladder)

            except BoardAddLadderError:
                pass

    def add_snake(self, snake: Snake) -> None:
        if not self.can_add_snake(snake):
            raise BoardAddSnakeError("Cannot add snake")

        self.validate_snake_with_start_point(snake)
        self.snakes.append(snake)

    def add_ladder(self, ladder: Ladder) -> None:
        if not self.can_add_ladder(ladder):
            raise BoardAddLadderError("Cannot add ladder")

        self.validate_ladder_with_start_point(ladder)
        self.ladders.append(ladder)

    def is_snake_chain_snake(self, snake: Snake) -> bool:
        return any(map(lambda old_snake: old_snake.head == snake.tail or
                                         old_snake.tail == snake.head, self.snakes))

    def is_ladder_chain_ladder(self, ladder: Ladder) -> bool:
        return any(map(lambda old_ladder: old_ladder.start == ladder.end or
                                          old_ladder.end == ladder.start, self.ladders))

    def is_snake_head_chain_ladder(self, snake: Snake) -> bool:
        return any(map(lambda ladder: ladder.play == snake.head, self.ladders))

    def is_ladder_start_chain_snake(self, ladder: Ladder) -> bool:
        return any(map(lambda snake: snake.head == ladder.start, self.snakes))

    def is_snake_tail_over_board_size(self, snake: Snake) -> bool:
        return snake.tail > self.size

    def is_snake_head_over_board_size(self, snake: Snake) -> bool:
        return snake.head > self.size

    def is_ladder_start_over_board_size(self, ladder: Ladder) -> bool:
        return ladder.start > self.size

    def is_ladder_end_over_board_size(self, ladder: Ladder) -> bool:
        return ladder.end > self.size

    def is_ladder_start_equal_board_size(self, ladder: Ladder) -> bool:
        return ladder.start == self.size

    def is_ladder_start_equal_finish_line(self, ladder: Ladder) -> bool:
        return ladder.start == self.finish_line

    def is_ladder_chain(self, ladder: Ladder):
        return (
                self.is_ladder_chain_ladder(ladder) or
                self.is_ladder_start_chain_snake(ladder)
                )

    def can_add_snake(self, snake: Snake) -> bool:
        return \
                not (
                        self.is_snake_chain_snake(snake)
                        or self.is_snake_head_chain_ladder(snake)
                        or self.is_snake_head_over_board_size(snake)
                        or self.is_snake_tail_over_board_size(snake)
                    )

    def can_add_ladder(self, ladder: Ladder) -> bool:
        return \
                not (
                        self.is_ladder_chain(ladder)
                        or self.is_ladder_start_over_board_size(ladder)
                        or self.is_ladder_end_over_board_size(ladder)
                        or self.is_ladder_start_equal_board_size(ladder)
                        or self.is_ladder_start_equal_finish_line(ladder)
                    )

    def get_snake_at_position(self, player_current_position: int) -> Optional[Snake]:
        snake = filter(lambda snake: snake.head == player_current_position, self.snakes)

        return next(snake, None)

    def get_ladder_at_position(self, player_current_position: int) -> Optional[Ladder]:
        ladder = filter(lambda ladder: ladder.start == player_current_position, self.ladders)

        return next(ladder, None)

    def set_player_position_at_start_point(self, player: Player) -> None:
        player.position = self.start_point

    def validate_snake_with_start_point(self, snake: Snake) -> None:
        if snake.head == self.start_point:
            raise HeadEqualStartPoint(self)

        if snake.head < self.start_point or snake.tail < self.start_point:
            raise SnakeSyntaxInputError(self)

    def validate_ladder_with_start_point(self, ladder: Ladder) -> None:
        if ladder.start == self.start_point or ladder.end == self.start_point:
            raise StartLadderOrEndLadderEqualStartPoint(self)

        if ladder.start < self.start_point or ladder.end < self.start_point:
            raise LadderSyntaxInputError(self)
