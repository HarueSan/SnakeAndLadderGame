from typing import List
from ladder import Ladder
from snake import Snake

class Board:

    def __init__(self, board_size: int, snakes: List[Snake] = [], ladders: List[Ladder] = []):
        self.size = board_size
        self.snakes: List[Snake] = snakes
        self.ladders: List[Ladder] = ladders