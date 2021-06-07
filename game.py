from player import Player
from board import Board
from random import randint
from typing import Union


class Game:

    def __init__(self, player: Player, board: Board) -> None:
        self.board = board
        self.player = player
        self.player.position = board.start_point

    def is_finish_game(self) -> bool:
        return self.player.position >= self.board.finish_line

    def play(self) -> None:
        print("*****Game start*****")
        print(f"Your first position is {self.player.position}\n")

        while True:
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

            if self.is_finish_game():
                break

            if not self.is_continue():
                break

        print("end game")

    def is_continue(self) -> bool:
        while True:
            answer = input("Continue play game? y/n: ")

            if answer == 'y' or answer == 'Y':
                return True

            elif answer == 'n' or answer == 'N':
                return False

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
        return bool(self.board.get_snake_at_position(self.player.position))

    def is_ladder_start(self) -> bool:
        return bool(self.board.get_ladder_at_position(self.player.position))
