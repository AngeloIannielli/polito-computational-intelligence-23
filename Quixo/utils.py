from copy import deepcopy
from itertools import product
from game import Game, Move
from enum import Enum
import random
import matplotlib.pyplot as plt

# define the corners
SIDES = [(0, 0), (0, 4), (4, 0), (4, 4)]


class HandleGame():    

    def possible_moves(currentGame: Game) -> tuple[tuple[int, int], Move]:

        # Copy to be sure it won't be modified
        copyCurrentGame = deepcopy(currentGame)
        
        # This list will contain all possibile moves
        possible_moves = []
        
        # Generate all possible combinations of the pieces' positions
        all_combinations = tuple(product(range(5), repeat=2))

        for straight_position in all_combinations:

            position = tuple((straight_position[1], straight_position[0]))
            
            # Evaluate if the taken piece is legit 
            # !!! (rules are taken from the code written in game.py)
            
            # acceptable only if in border
            acceptable: bool = (
                # check if it is in the first row
                (position[0] == 0 and position[1] < 5)
                # check if it is in the last row
                or (position[0] == 4 and position[1] < 5)
                # check if it is in the first column
                or (position[1] == 0 and position[0] < 5)
                # check if it is in the last column
                or (position[1] == 4 and position[0] < 5)
                # and check if the piece can be moved by the current player
            ) and (copyCurrentGame._board[position] < 0 or copyCurrentGame._board[position] == copyCurrentGame.current_player_idx)
            
            if acceptable:
                # print("Acceptable:", "MiniMaxID", copyCurrentGame.current_player_idx, "pedina", copyCurrentGame._board[position], "taken at", position)
                # Generate the combination of moves, according to the rules written in game.py
                
                # if the piece position is not in a corner
                if position not in SIDES:
                    
                    # if it is at the TOP, it can be moved down, left or right
                    if position[0] == 0:
                        possible_moves.append((straight_position, Move.BOTTOM))
                        possible_moves.append((straight_position, Move.LEFT))
                        possible_moves.append((straight_position, Move.RIGHT))
    
                    # if it is at the BOTTOM, it can be moved up, left or right
                    if position[0] == 4:
                        possible_moves.append((straight_position, Move.TOP))
                        possible_moves.append((straight_position, Move.LEFT))
                        possible_moves.append((straight_position, Move.RIGHT))
                    
                    # if it is on the LEFT, it can be moved up, down or right
                    if position[1] == 0:
                        possible_moves.append((straight_position, Move.BOTTOM))
                        possible_moves.append((straight_position, Move.TOP))
                        possible_moves.append((straight_position, Move.RIGHT))
                    
                    # if it is on the RIGHT, it can be moved up, down or left
                    if position[1] == 4:
                        possible_moves.append((straight_position, Move.BOTTOM))
                        possible_moves.append((straight_position, Move.TOP))
                        possible_moves.append((straight_position, Move.LEFT))
                    
                # if the piece position is in a corner
                else:
                    
                    # if it is in the upper left corner, it can be moved to the right and down
                    if position == (0, 0):
                        possible_moves.append((straight_position, Move.BOTTOM))
                        possible_moves.append((straight_position, Move.RIGHT))
                        
                    # if it is in the lower left corner, it can be moved to the right and up
                    if position == (4, 0):
                        possible_moves.append((straight_position, Move.TOP))
                        possible_moves.append((straight_position, Move.RIGHT))
                    
                    # if it is in the upper right corner, it can be moved to the left and down
                    if position == (0, 4):
                        possible_moves.append((straight_position, Move.BOTTOM))
                        possible_moves.append((straight_position, Move.LEFT))
                    
                    # if it is in the lower right corner, it can be moved to the left and up
                    if position == (4, 4):
                        possible_moves.append((straight_position, Move.TOP))
                        possible_moves.append((straight_position, Move.LEFT))

            
        # Return a tuple for efficiency 
        random.shuffle(possible_moves)               
        return tuple(possible_moves)
                    


def plot_results(wins, losses, title):
    labels = ['Victories', 'Defeats']
    values = [wins, losses]

    x = range(len(labels))

    plt.bar(x, values, color=['green', 'red'])

    plt.xticks(x, labels)

    plt.title(title)
    
    plt.ylabel('Number of matches')

    plt.show()

