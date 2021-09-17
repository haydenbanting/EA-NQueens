#----------------------------------------------------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt 
from population import phenotype
from population import crossover
from population import mutation

#----------------------------------------------------------------------------------------------------------------------#
# Parameters
#----------------------------------------------------------------------------------------------------------------------#
grid_size = 8
pop_size = 500
num_parents = 10
num_offspring = 4
mutation_rate = 0.2
cross_over_rate = 1.0
max_generations = 5000
prints = True
plots = True

#----------------------------------------------------------------------------------------------------------------------#
# Parameter sanity check
#----------------------------------------------------------------------------------------------------------------------#
assert(num_parents >= num_offspring)



#----------------------------------------------------------------------------------------------------------------------#
# Initialize population
#----------------------------------------------------------------------------------------------------------------------#
population = []
for i in range(pop_size):
    population.append( phenotype.Phenotype( np.random.randint(8, size=8) ) )
    #population.append( phenotype.Phenotype( np.random.permutation( np.arange(grid_size) ) ) )

# Pre-sort population for faster processing in EA
population.sort(key=lambda x: x.fitness)

#----------------------------------------------------------------------------------------------------------------------#
# Evolutionary algorithm
#----------------------------------------------------------------------------------------------------------------------#

generation = 0
best_fitness = population[0].fitness
pop_ave_fitness = []

# Loop until solution is found or after a certain number of iterations
while (generation < max_generations) and (best_fitness > 0):

    generation += 1
    #parent_candidates = []
    
    #------------------------------------------------------------------------------------------------------------------#
    # Parent Selection
    #------------------------------------------------------------------------------------------------------------------#

    # Pick candidate parents
    parent_cand_idxs = np.random.randint(pop_size, size=5)
    parent_candidates = [population[i] for i in parent_cand_idxs]

    # Sort the candidates by fitness
    parent_candidates.sort(key=lambda x: x.fitness)

    # Keep only best parents
    parents = [parent_candidates[i] for i in range(num_offspring)]

    #------------------------------------------------------------------------------------------------------------------#
    # Crossover 
    #------------------------------------------------------------------------------------------------------------------#
    offspring = []
    # Loop over all parent pairs
    for i in range(len(parents)-1):
        for j in range(i+1, len(parents)):
            
            # Check if cross-over will occur for this pair    
            if (np.random.uniform(0, 1) <= cross_over_rate): 
                offspring += crossover.crossover(parents[i], parents[j], grid_size) 

    #------------------------------------------------------------------------------------------------------------------#
    # Mutation
    #------------------------------------------------------------------------------------------------------------------#

    # Loop over each offspring
    for i in range(len(offspring)):

        # Check if mutation will occur
        if (np.random.uniform(0, 1) <= mutation_rate): 
            offspring[i] = mutation.mutate(offspring[i], grid_size)


    #------------------------------------------------------------------------------------------------------------------#
    # Update population
    #------------------------------------------------------------------------------------------------------------------#

    # Add offspring to population
    for i in range(len(offspring)):

        # Insert them into sorted population
        for j in range(len(population)):
            #print(j)
            if (offspring[i].fitness < population[j].fitness):
                population.insert(j, offspring[i]) 
                break
            elif (j == len(population) - 1): # edge
                population.insert(j, offspring[i])
            #elif (j == len(o))
    
    # Remove worst candidates in population
    population = population[:len(population) - len(offspring)]

    # Keeping population size contant each generation
    assert(len(population) == pop_size)

    #------------------------------------------------------------------------------------------------------------------#
    # Population evaluation
    #------------------------------------------------------------------------------------------------------------------#
    
    # Compute average fitness of the population
    s = 0
    for i in range(len(population)): s += population[i].fitness
    ave = s / pop_size
    pop_ave_fitness.append(ave)

    # Get new best fitness
    best_fitness = population[0].fitness

    #------------------------------------------------------------------------------------------------------------------#
    # Optional prints about generation
    #------------------------------------------------------------------------------------------------------------------#
    if prints:
        print('Generation: {:4d} Population Size: {:3d} Average Fitness: {:.2f} Best Phenotype: {} Fitness: {}'.format(generation, len(population), ave, population[0].genotype, population[0].fitness))
    

#------------------------------------------------------------------------------------------------------------------#
# Optional plots
#------------------------------------------------------------------------------------------------------------------#
if plots:
    plt.figure(1)
    plt.plot([i for i in range(generation)], pop_ave_fitness, color='b', linestyle='-', linewidth=2)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.ylabel('Population Average Fitness', fontsize=14)
    plt.xlabel('Generation', fontsize=14)
    plt.show()
    








