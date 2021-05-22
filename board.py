from typing import List
from ladder import Ladder
from snake import Snake

class BoardException(Exception):
    pass
        
class Board:

    def __init__(self, board_size: int):
        self.size = board_size
        self.snakes: List[Snake] = []
        self.ladders: List[Ladder] = []
    
    def add_snake(self, snake: Snake) -> None:
        if not self.can_add_snake(snake):
            raise BoardException("Can't add snake")

        self.snakes.append(snake)

    def add_ladder(self, ladder: Ladder) -> None:
        if not self.can_add_ladder(ladder):
            raise BoardException("Can't add ladder")
            
        self.ladders.append(ladder)
    
    def is_snake_chain_snake(self, snake: Snake) -> bool:
        return any(map(lambda old_snake: old_snake.head == snake.tail or 
                old_snake.tail == snake.head, self.snakes))
        
    def is_ladder_chain_ladder(self, ladder: Ladder) -> bool:
        return any(map(lambda old_ladder: old_ladder.start == ladder.end or 
                old_ladder.end == ladder.start, self.ladders))

    def is_head_snake_chain_ladder(self, snake: Snake) -> bool:
        return any(map(lambda ladder: ladder.start == snake.head, self.ladders))
    
    def is_start_ladder_chain_snake(self, ladder: Ladder) -> bool:
        return any(map(lambda snake: snake.head == ladder.start, self.snakes))

    def can_add_snake(self, snake: Snake) -> bool:
        if self.is_snake_chain_snake(snake) or self.is_head_snake_chain_ladder(snake):
            return False

        return True
    
    def can_add_ladder(self, ladder: Ladder) -> bool:
        if self.is_ladder_chain_ladder(ladder) or self.is_start_ladder_chain_snake(ladder):
            return False
        
        return True
    