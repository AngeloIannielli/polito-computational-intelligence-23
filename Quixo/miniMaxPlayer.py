import random
from utils import HandleGame
from game import Game, Move, Player
from copy import deepcopy
from enum import Enum
import numpy as np

POINTS = [0, 0, 5, 20, 50, 1000]
POINTS_DIAGONAL = [0, 1, 5, 20, 50, 1000]

class MinOrMax(Enum):
    isMin = -1
    isMax = 1

class MiniMaxPlayer(Player):
    def __init__(self, max_depth) -> None:
        super().__init__()
        self.max_depth = max_depth
        self.name = "MiniMax"
    
    def evaluate_state(self, currentGame: 'Game', min_or_max: MinOrMax):
        
        # Check if the game is over, returning an infinite value coeherent with the min or max sign
        # if currentGame.check_winner() >=0 : return float("inf")*min_or_max.value
        
        # The player who made the last move, who is waiting for the value
        player_ID = currentGame.current_player_idx + 1
        player_ID %= 2
        
        # The current player
        opponent_ID = currentGame.current_player_idx
        
        # Count the number of pieces in a row and in a column, for each one
        player_pieces_on_row = np.sum(currentGame._board == player_ID, axis=1)
        player_pieces_on_column = np.sum(currentGame._board == player_ID, axis=0)

        # Count the number of pieces in a row and in a column, for each one
        opponent_pieces_on_row = np.sum(currentGame._board == opponent_ID, axis=1)
        opponent_pieces_on_column = np.sum(currentGame._board == opponent_ID, axis=0)
        
        # Inizialize the value
        value = 0

        # Assign the score. The longer the sequence the "higher" the score.
        
        # It is needed to change the sign because this points promote the previuos player (opposite to the value of the current min_or_max flag)
        for sequence in player_pieces_on_row:
            value += POINTS[sequence]*min_or_max.value*(-1)
        for sequence in player_pieces_on_column:
            value += POINTS[sequence]*min_or_max.value*(-1)
        
        # Points for the current player
        for sequence in opponent_pieces_on_row:
            value += POINTS[sequence]*min_or_max.value
        for sequence in opponent_pieces_on_column:
            value += POINTS[sequence]*min_or_max.value
        
        # Count the number of pieces on diagonals
        player_pieces_on_first_diag = np.sum(np.diag(currentGame._board) == player_ID)
        player_pieces_on_second_diag = np.sum(np.diag(np.fliplr(currentGame._board)) == player_ID)
        opponent_pieces_on_first_diag = np.sum(np.diag(currentGame._board) == opponent_ID)
        opponent_pieces_on_second_diag = np.sum(np.diag(np.fliplr(currentGame._board)) == opponent_ID)
        
        value += POINTS_DIAGONAL[player_pieces_on_first_diag]*min_or_max.value*(-1)
        value += POINTS_DIAGONAL[player_pieces_on_second_diag]*min_or_max.value*(-1)
        value += POINTS_DIAGONAL[opponent_pieces_on_first_diag]*min_or_max.value
        value += POINTS_DIAGONAL[opponent_pieces_on_second_diag]*min_or_max.value
        
        return value
    
        
    def apply_minimax_algorithm(self, currentGame: 'Game', depth, min_or_max, alpha, beta):
        
        # End of the iterative calls
        # Check if it arrived in the max depth or the game is over
        if depth == 0 or currentGame.check_winner() >= 0:
            return self.evaluate_state(currentGame, min_or_max), alpha, beta
        
        # Decrese the current depth
        current_depth = depth - 1
        
        # Get the ID of the current player
        player_ID = currentGame.get_current_player()
        
        # Check if the player is the maximising one
        if min_or_max == MinOrMax.isMax :
            
            # Set the best value as the worst possible 
            best_value = float('-inf')
            
            for move in HandleGame.possible_moves(currentGame):
                
                # Generate a copy of the game, able to be modified in the iteration
                newGame = deepcopy(currentGame)

                # Apply the current move
                newGame.moves(move[0], move[1], player_ID)
                newGame.current_player_idx += 1
                newGame.current_player_idx %= 2
                                
                # Reiterate the recursive algorithm
                value, alpha, beta = self.apply_minimax_algorithm(newGame, current_depth, MinOrMax.isMin, alpha, beta)
                
                # Update the best value
                # best_value = value if value > best_value else best_value
                if value > best_value:
                    best_value = value
                                
                # Handle alpha-beta pruning
                alpha = value if value > alpha else alpha
                if alpha >= beta:
                    break
                
                if best_value == float("inf"): break
                
            return best_value, alpha, beta
        
        # The player is minimising one
        else:
            
            # Set the best value as the worst possible 
            best_value = float('inf')
            
            for move in HandleGame.possible_moves(currentGame):
                
                # Generate a copy of the game, able to be modified in the iteration
                # newGame = deepcopy(currentGame)
                newGame = Game()
                newGame._board = deepcopy(currentGame._board)
                
                # Apply the current move
                newGame.moves(move[0], move[1], player_ID)
                newGame.current_player_idx += 1
                newGame.current_player_idx %= 2
                
                # Reiterate the recursive algorithm
                value, alpha, beta = self.apply_minimax_algorithm(newGame, current_depth, MinOrMax.isMax, alpha, beta)
                
                # Update the best value
                # best_value = value if value < best_value else best_value
                if value < best_value:
                    best_value = value
                
                # Handle alpha-beta pruning
                beta = value if value < beta else beta
                if alpha >= beta:
                    break
                
                if best_value == float("-inf"): break
                
            return best_value, alpha, beta
        
    
    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        
        # Generate all possible legit moves
        possible_moves = HandleGame.possible_moves(game)
        # Find the best move, by testing all in the following max_depth moves. 
        # If the game is not ended in maz_depth moves, it continues randomly to reduce the run time.
                
        best_move = None
        best_value = float("-inf")
        
        # Lookin for the best move
        for move in possible_moves:
            
            # Generate a copy of the game, able to be modified in the iteration
            newGame = deepcopy(game)

            # Apply the current move
            newGame.moves(move[0], move[1], game.current_player_idx)
            
            if newGame.check_winner() == newGame.current_player_idx :
                best_move = move
                best_value = float("inf")
                break
            
            newGame.current_player_idx += 1
            newGame.current_player_idx %= 2

            # Apply the minimax algorithm
            value, alpha, beta = self.apply_minimax_algorithm(newGame, self.max_depth, MinOrMax.isMin, -float("inf"), float("inf"))
            
            # Update the results
            # best_value, best_move = (value, move) if value > best_value else (best_value, best_move)
            if value > best_value:
                best_value = value
                best_move = move

        return best_move