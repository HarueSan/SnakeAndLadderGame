from typing import Optional
from player import Player
from board import Board
from snake import Snake
from ladder import Ladder

class Game:

    def __init__(self, player: Player, board: Board) -> None:
        self.board = board
        self.player = player

    def is_finished(self) -> bool:
        return self.player.position == self.board.size

    def start(self) -> None:
        while not self.is_finished() :
            no_dice = self.toss_dice() 
            self.move_forward(no_dice)

            if self.is_start_ladder():
                self.move_to_end_ladder()

            elif self.is_head_snake():
                self.move_to_tail_snake()
            
            print(f"Your current position is {self.player.position}")

        print("end game")
            
    def toss_dice(self) -> int:
        return int(input("Dice: "))
            
    def move_forward(self, step: int) -> None:
        self.player.position += step

        if self.player.position > self.board.size:
            self.move_backward()

    def move_backward(self):
        self.player.position = self.board.size - (self.player.position - self.board.size)
        
    def move_to_tail_snake(self) -> None:
        snake = self.get_snake_at_current_position()

        if snake:
            self.player.position = snake.tail
    
    def move_to_end_ladder(self) -> None:
        ladder = self.get_ladder_at_current_position()

        if ladder:
            self.player.position = ladder.end
    
    def is_head_snake(self) -> bool:
        if self.get_snake_at_current_position():
            return True
        
        return False
    
    def is_start_ladder(self) -> bool:
        if self.get_ladder_at_current_position():
            return True
        
        return False
    
    # should move this function to Board?
    def get_snake_at_current_position(self) -> Optional[Snake]:
        player_current_position = self.player.position
        snake = filter(lambda snake: snake.head == player_current_position, self.board.snakes)
        
        return next(snake, None)
        
    # should move this function to Board?
    def get_ladder_at_current_position(self) -> Optional[Ladder]:
        player_current_position = self.player.position
        ladder = filter(lambda ladder: ladder.start == player_current_position, self.board.ladders)

        return next(ladder, None)
        