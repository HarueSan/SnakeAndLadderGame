from typing import List
from board import Board
from snake import Snake
from ladder import Ladder
from player import Player
from game import Game

def read_snakes(filename) -> List[Snake]:
    file = open(filename)
    snakes = []

    for line in file :
        snake_values = line.split()
        head = int(snake_values[0])
        tail = int(snake_values[1])
        snakes.append(Snake(head, tail))

    file.close()

    return snakes

def read_ladders(filename) -> List[Ladder] :
    file = open(filename)
    ladders = []

    for line in file :
        ladder_values = line.split()
        start = int(ladder_values[0])
        end = int(ladder_values[1])
        ladders.append(Ladder(start, end))

    file.close()

    return ladders

def main():
    snake_file = 'snakes.txt'
    ladder_file = 'ladders.txt'
    snakes = read_snakes(snake_file)
    ladders = read_ladders(ladder_file)

    board_size = 100
    finish_line = 100

    board = Board(board_size, finish_line, ladders, snakes)
   
    player = Player()
    game = Game(player, board)
    game.start()
    
if __name__ == "__main__" :
    main()
    