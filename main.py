# use PyCharm format
from typing import List
from board import Board
from snake import Snake
from ladder import Ladder
from player import Player
from game import Game


def read_snakes(filename) -> List[Snake]:
    file = open(filename)
    snakes = []

    for line in file:
        snake_values = line.split()
        head = int(snake_values[0])
        tail = int(snake_values[1])
        snakes.append(Snake(head, tail))

    file.close()

    return snakes


def read_ladders(filename) -> List[Ladder]:
    file = open(filename)
    ladders = []

    for line in file:
        ladder_values = line.split()
        start = int(ladder_values[0])
        end = int(ladder_values[1])
        ladders.append(Ladder(start, end))

    file.close()

    return ladders


def read_players(filename) -> List[Player]:
    file = open(filename)
    players = []

    for line in file:
        player_values = line.split()
        player_name = player_values[0]
        players.append(Player(player_name))

    file.close()

    return players


def main():
    snake_file = 'snakes.txt'
    ladder_file = 'ladders.txt'
    players_file = 'players.txt'
    snakes = read_snakes(snake_file)
    ladders = read_ladders(ladder_file)
    players = read_players(players_file)

    board_size = 100
    start_point = 1
    finish_line = 100

    board = Board(start_point, board_size, finish_line, ladders, snakes)
    game = Game(players, board)

    game.play()


if __name__ == "__main__":
    main()
