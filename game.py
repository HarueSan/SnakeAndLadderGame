from player import Player
from board import Board

class Game:

    def __init__(self, player: Player, board: Board) -> None:
        self.board = Board()
        self.player = Player()

    def is_finished(self) -> bool:
        pass

    def start(self, step: int) -> None:
        while not self.is_finished() :
            pass

    def move_forward(self, step: int) -> None:
        pass
    
    def move_backward(self) -> None:
        pass
    
    def is_normal_block(self) -> bool:
        pass
    
    # TODO: rename from sneck -> snake
    def is_head_sneck(self) -> bool:
        pass
    
    def is_start_ladder(self) -> bool:
        pass