from player import Player
from board import Board
from random import randint


class Game:

    def __init__(self, player: Player, board: Board) -> None:
        self.board = board
        self.player = player

    def is_finish_game(self) -> bool:
        return self.player.position >= self.board.finish_line

    def start(self) -> None:
        # TODO: เปลี่ยนให้รับได้ทั้ง Y ด้วย
        answer = 'y'

        print("*****Game start*****")
        print(f"Your first position is {self.player.position}\n")

        while answer == 'y' and not self.is_finish_game():
            dice_number = self.random_dice_number()

            print(f"The dice number is {dice_number}")
            self.move_player_forward(dice_number)
        
            if self.is_ladder_start():
                print("Lucky!! You found ladder")
                self.move_player_to_ladder_end()

            elif self.is_snake_head():
                print("Unlucky!! You were bitten by snake")
                self.move_player_to_snake_tail()
            
            print(f"Your current position is {self.player.position}\n")
            answer = input("Continue play game? y/n: ")

        print("end game")

    def random_dice_number(self) -> int:
        return randint(1, 6)
            
    def move_player_forward(self, dice_number: int) -> None:
        self.player.position += dice_number

    def move_player_to_snake_tail(self) -> None:
        snake = self.board.get_snake_at_position(self.player.position)
        self.player.position = snake.tail

    def move_player_to_ladder_end(self) -> None:
        ladder = self.board.get_ladder_at_position(self.player.position)
        self.player.position = ladder.end

    def is_snake_head(self) -> bool:
        # TODO: ครอบ bool ให้ self.board.get_snake_at_position(self.player.position)
        return True if self.board.get_snake_at_position(self.player.position) else False

    def is_ladder_start(self) -> bool:
        # TODO: ครอบ bool ให้ self.board.get_snake_at_position(self.player.position)
        return True if self.board.get_ladder_at_position(self.player.position) else False
