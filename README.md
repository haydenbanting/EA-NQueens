# Evolutionary Algoirthm to find Solutions to the 8 Queens Problem

The 8 Queens problem asks to find an arrangement of 8 queens on an 8x8 chess board in which no queen 'checks' another. This solution is generalized to solve the N-Queens problem on an NxN grid. 

The user can tune several algorithm parameters:

grid_size - size of the grid <br/>
pop_size - size of the population of candidate solutions <br/>
num_parents - number of parents to use in the selection phase <br/>
num_offspring - number of offspring produced each generation <br/>
crossover_rate - chance an offspring obtains geno from both parents <br/>
mutation_rate - chance of mutation per generation per offsrping <br/>
max_generations - stop after this number of generations if no solution is found <br/>
  
Also some options to see various prints and plots about the process.

Example solution:

[7 3 0 2 5 1 6 4]

<img src="https://github.com/haydenbanting/ea-8queens/blob/main/output/solution.png" width="400" height="400">




  
