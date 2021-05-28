from typing import List, Optional
from ladder import Ladder
from snake import Snake
from board_error import BoardExceptionError

class Board:

    # TODO: ระบุ type ของ list
    def __init__(self, board_size: int, finish_line: int, ladders: list,  snakes: list):
        self.size = board_size
        self.finish_line = finish_line
        self.snakes: List[Snake] = []
        self.ladders: List[Ladder]  = []

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

    # TODO: return if ไปเลยก็ได้
    def can_add_snake(self, snake: Snake) -> bool:
        if self.is_snake_chain_snake(snake) or self.is_snake_head_chain_ladder(snake):
            return False

        return True
    
    # TODO: return if ไปเลยก็ได้
    def can_add_ladder(self, ladder: Ladder) -> bool:
        if self.is_ladder_chain_ladder(ladder) or self.is_ladder_start_chain_snake(ladder):
            return False
        
        return True
    
    # TODO: ลบคำว่า current ในชื่อฟังก์ชันออก
    def get_snake_at_current_position(self, player_current_position: int) -> Optional[Snake]:
        snake = filter(lambda snake: snake.head == player_current_position, self.snakes)
        
        return next(snake, None)
    
    # TODO: ลบคำว่า current ในชื่อฟังก์ชันออก
    def get_ladder_at_current_position(self, player_current_position: int) -> Optional[Ladder]:
        ladder = filter(lambda ladder: ladder.start == player_current_position, self.ladders)

        return next(ladder, None)
    