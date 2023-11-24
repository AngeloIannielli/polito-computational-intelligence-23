Here, the links of my reviews

https://github.com/Federica000/Computational-Intelligence/issues/4

https://github.com/RaffaeleViola/computational-intelligence/issues/3

# Review 1

HI! I chose your lab randomly from the file containing the CI course github links.

## Introduction

I'll start by saying that you've created a nice genetic algorithm, quite complex and perhaps for this reason it took me some time to fully understand what the logic of the code was.

If I understand correctly, your goal was to create a population of individuals containing a set of states and a move for each of them. The latest generation should contain sets of optimal actions to carry out in case, during the game, the system ricognizes an already known state. Even if I understand correctly, the knowledge of the algorithm is divided into the various individuals, who are not "independent" but must collaborate to provide an ideal move.

## My doubts

The idea is very particular and I liked it a lot, but there are some points that are unclear to me.

-  In the _play_ function, on the line 
`if state == nim_game:` 
I'm afraid that the comparison will never be successful due to the different representation of the two variables. Running the code it seems to me that it never enters the true condition.

- I've the doubt that the algorithm prefers moves that lead to an nim XOR = 0 (which should be exactly the condition to discard). In the last generation, in fact, I saw many moves that, associated with the state, cause an xor equal to zero.

## Advice

 - As advice for a hypothetical future development, it would be interesting to try not to have redundancy within the final generation (therefore managing each state once by choosing only one move).

- It might be useful to include a little more comments in the code, just because the algorithm is quite complex.

## Conclusion

To conclude, I think you have done an original and different job compared to the others. I really appreciated seeing a different approach.

I hope I have understood your code correctly and if not, I apologize for exposing my doubts to you.

_Good luck for the next works, keep it up_ 😉​

# Review 2

HI! I chose your lab randomly from the file containing the CI course github links.

## My point of view and suggestions

I'll start by saying that I found the code very readable and well structured.

Since we have some commonalities, I want to share with you some tips (some of which I applied in my own code, some I received from other reviewers)

- To avoid training the system on a single challenger (the optimal) you risk having a result with a starting bias. I did the same thing in my code, but it certainly can be interesting to evaluate it through challenges with other individuals and/or strategies.

- Even though the code is linear, it might be useful to have some more comments.

- I appreciated the progress bar which allows you to see how far along the execution of the algorithm is. However, it would be nice to also print some additional information.

_Good luck for the next works, keep it up_ 😉