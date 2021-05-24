from player import Player
from board import Board

class Game:

    def __init__(self, player: Player, board: Board) -> None:
        self.board = board
        self.player = player

    def is_finish_game(self) -> bool:
        return self.player.position == self.board.size

    def start(self) -> None:
        while not self.is_finish_game() :
            dice_number = self.toss_dice() 
            self.move_forward(dice_number)
        
            if self.is_ladder_start():
                print("Lucky!! You found ladder")
                self.move_to_ladder_end()

            elif self.is_snake_head():
                print("Unlucky!! You were bitten by snake")
                self.move_to_snake_tail()
            
            print(f"Your current position is {self.player.position}")

        print("end game")
            
    def toss_dice(self) -> int:
        return int(input("Dice: "))
            
    def move_forward(self, dice_number: int) -> None:
        self.player.position += dice_number

        if self.player.position > self.board.size:
            self.move_backward()

    def move_backward(self):
        self.player.position = self.board.size - (self.player.position - self.board.size)
        
    def move_to_snake_tail(self) -> None:
        snake = self.board.get_snake_at_current_position(self.player.position)

        if snake:
            self.player.position = snake.tail
    
    def move_to_ladder_end(self) -> None:
        ladder = self.board.get_ladder_at_current_position(self.player.position)

        if ladder:
            self.player.position = ladder.end
    
    def is_snake_head(self) -> bool:
        if self.board.get_snake_at_current_position(self.player.position):
            return True
        
        return False
    
    def is_ladder_start(self) -> bool:
        if self.board.get_ladder_at_current_position(self.player.position):
            return True
        
        return False
        