# Quixo game

## Introduction
The final project requires implementing a player capable of playing Quixo. It's a game played on a 5x5 grid of cubes, with each cube having two symbols: a circle and a cross, and empty faces. Players take turns choosing a cube (whether it belongs to them or is unclaimed, with the empty face facing up), rotating it to display their symbol, and then pushing it into the empty square, thereby moving all adjacent cubes in the same direction. If a player creates an alignment of 5 symbols, they win the game.

In the code, the cross and circle are represented by 0 and 1, and the empty face by -1.

## My Idea
I've implemented a minimax algorithm: therefore, my player can evaluate all possible moves and choose the most promising one.

To do this, I've developed the recursive function apply_minimax_algorithm: during evaluation, the player starts from the current game state and assumes that each player will play in the best way to maximize their chance of winning (and minimize their opponent's).

To assign a value to the considered state, I've used the evaluate_state function. It's based on a heuristic I devised, where more points are awarded as the player achieves longer alignments of aligned squares. Specifically, I've assigned 5 points for 2 aligned pieces, 20 for three pieces, 50 for four, and 1000 for five (which equals a win). I've also favored selection on diagonals by giving an additional point if the piece is on one.

Since processing times were very long, I added Alpha-beta pruning: this allows discarding less promising branches of the tree.

The function that generates possible moves relies entirely on the checks made within the module provided by the task.