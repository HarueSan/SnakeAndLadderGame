# TODO: ให้สร้างบอร์ดได้ แม้จะมี ladder หรือ snake พัง
from typing import List, Optional
from ladder import Ladder
from snake import Snake
from error import *


class Board:

    def __init__(self, board_size: int, finish_line: int, ladders: List[Ladder], snakes: List[Snake]):
        self.size = board_size
        self.finish_line = finish_line
        self.snakes: List[Snake] = []
        self.ladders: List[Ladder] = []

        # ************ #
        for snake in snakes: self.add_snake(snake)
        for ladder in ladders: self.add_ladder(ladder)

    def add_snake(self, snake: Snake) -> None:
        if not self.can_add_snake(snake):
            raise BoardExceptionError("Can't add snake")

        self.snakes.append(snake)

    def add_ladder(self, ladder: Ladder) -> None:
        if not self.can_add_ladder(ladder):
            raise BoardExceptionError("Can't add ladder")

        self.ladders.append(ladder)

    def is_snake_chain_snake(self, snake: Snake) -> bool:
        return any(map(lambda old_snake: old_snake.head == snake.tail or
                                         old_snake.tail == snake.head, self.snakes))

    def is_ladder_chain_ladder(self, ladder: Ladder) -> bool:
        return any(map(lambda old_ladder: old_ladder.start == ladder.end or
                                          old_ladder.end == ladder.start, self.ladders))

    def is_snake_head_chain_ladder(self, snake: Snake) -> bool:
        return any(map(lambda ladder: ladder.start == snake.head, self.ladders))

    def is_ladder_start_chain_snake(self, ladder: Ladder) -> bool:
        return any(map(lambda snake: snake.head == ladder.start, self.snakes))

    def can_add_snake(self, snake: Snake) -> bool:
        if \
                self.is_snake_chain_snake(snake) or self.is_snake_head_chain_ladder(snake)\
                or snake.tail > self.size or snake.head > self.size\
                or snake.head == self.finish_line:
            return False

        return True

    def can_add_ladder(self, ladder: Ladder) -> bool:
        if \
                self.is_ladder_chain_ladder(ladder) or self.is_ladder_start_chain_snake(ladder) \
                or ladder.start > self.size or ladder.end > self.size\
                or ladder.start == self.size or ladder.start == self.finish_line:

            return False

        return True

    def get_snake_at_position(self, player_current_position: int) -> Optional[Snake]:
        snake = filter(lambda snake: snake.head == player_current_position, self.snakes)

        return next(snake, None)

    def get_ladder_at_position(self, player_current_position: int) -> Optional[Ladder]:
        ladder = filter(lambda ladder: ladder.start == player_current_position, self.ladders)

        return next(ladder, None)
