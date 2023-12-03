# Lab 9

## Problem
The problem we need to solve is to optimize the fitness of our solution, minimizing the number of fitness calls. We should consider it as a _black box_ so the extra information that the best solution is composed by all 1 will be ignored. 

## My idea
I tried to implement an algorithm that use the concept of _"islands"_ to group the solutions with similar values of fitness. To do this I implemented this things:

- An archipelago, that is a list of island (3 in my algorithm)
- The islands, that have some parameters to define their own population capacity, their mutation rate, the number of parents needed to have a new individual, the size of tournament (for the parent selection) and the interval of allowed fitness.
- The individuals, that have 2 different ways to be created: the first one is random and it is used only to generate the first population, the second consists in a xover between the parents and a mutation (according to the island mutation rate). 
