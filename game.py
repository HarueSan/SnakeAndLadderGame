from player import Player
from board import Board
from random import randint
from typing import Union, List


class Game:

    def __init__(self, players: List[Player], board: Board) -> None:
        self.board = board
        self.players: List[Player] = players
        self.set_players_at_start_point(self.players)

    def set_players_at_start_point(self, players: List[Player]) -> None:
        for player in players:
            player.position = self.board.start_point

    def play(self) -> None:
        anyone_win = False
        players = self.players.copy()

        while not anyone_win and len(players) > 0:
            for player in players:
                if self.is_continue(player):
                    dice_number = self.random_dice_number()

                    print(f"{player.name} dice number: {dice_number}")
                    self.move_forward(dice_number, player)

                    if self.is_ladder_start(player):
                        self.move_to_ladder_end(player)

                    if self.is_snake_head(player):
                        self.move_to_snake_tail(player)

                    print(f"{player.name} position: {player.position}")

                    if self.is_win(player):
                        anyone_win = True
                        print(f"{player.name} win!")
                        break
                else:
                    players.remove(player)

    def is_win(self, player: Player) -> bool:
        return player.position >= self.board.finish_line

    def is_continue(self, player: Player) -> bool:
        while True:
            answer = input(f"{player.name} continue? y/n: ")

            if answer == 'y' or answer == 'Y':
                return True

            elif answer == 'n' or answer == 'N':
                return False

    def random_dice_number(self) -> int:
        return randint(1, 6)

    def move_forward(self, dice_number: int, player: Player) -> None:
        player.position += dice_number

    def move_to_snake_tail(self, player: Player) -> None:
        snake = self.board.get_snake_at_position(player.position)
        player.position = snake.tail

    def move_to_ladder_end(self, player: Player) -> None:
        ladder = self.board.get_ladder_at_position(player.position)
        player.position = ladder.end

    def is_snake_head(self, player: Player) -> bool:
        return bool(self.board.get_snake_at_position(player.position))

    def is_ladder_start(self, player: Player) -> bool:
        return bool(self.board.get_ladder_at_position(player.position))
