import random
from utils import HandleGame
from game import Game, Move, Player
from miniMaxPlayer import MiniMaxPlayer
from tqdm import tqdm
from utils import plot_results


class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Random"

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move



if __name__ == '__main__':
    
    g = Game()
    player1 = MiniMaxPlayer(1)
    player2 = RandomPlayer()
    winner = g.play(player2, player1)
    g.print()
    print(f"Winner: Player {winner}")
    
    miniMax_wins_first = 0
    
    with tqdm(total=100, desc="Partite giocate") as pbar:
        for match in range(100):
            g = Game()
            player1 = MiniMaxPlayer(6)
            player2 = RandomPlayer()
            winner = g.play(player1, player2)
            if winner == 0 : miniMax_wins_first += 1
            
            pbar.update(1)
            
    print("MiniMax wins", miniMax_wins_first, "matches on 100 (first player to move)")
        
    miniMax_wins_second = 0
    
    with tqdm(total=100, desc="Partite giocate") as pbar:
        for match in range(100):
            g = Game()
            player1 = MiniMaxPlayer(14)
            player2 = RandomPlayer()
            winner = g.play(player2, player1)
            if winner == 1 : miniMax_wins_second += 1
            
            pbar.update(1)
            
    plot_results(miniMax_wins_first, 100 - miniMax_wins_first, "MiniMax is starting")
    plot_results(miniMax_wins_second, 100 - miniMax_wins_second, "Random is starting")

    print("MiniMax wins", miniMax_wins_second, "matches on 100 (second player to move)")
        
   
        
