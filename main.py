#----------------------------------------------------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt 
from population import phenotype
from population import crossover
from population import mutation
from population import selection
from population import survival

#----------------------------------------------------------------------------------------------------------------------#
# Parameters
#----------------------------------------------------------------------------------------------------------------------#
grid_size = 16              
pop_size = 250            
selection_size = 50         
num_parents = 100          
num_offspring = 100          
mutation_rate = 0.4         
cross_over_rate = 1    
max_generations = 5000     
prints = True
plots = True

#----------------------------------------------------------------------------------------------------------------------#
# Parameter sanity check
#----------------------------------------------------------------------------------------------------------------------#
assert(pop_size > num_parents)
assert(num_parents >= num_offspring)  
assert(num_parents % 2 == 0)            
assert(num_offspring % 2 == 0)

#----------------------------------------------------------------------------------------------------------------------#
# Initialize population
#----------------------------------------------------------------------------------------------------------------------#

# Random permutation initialization
population = [phenotype.Phenotype(np.random.permutation(np.arange(grid_size))) for i in range(pop_size)]

# Pre-sort population for faster processing in EA
population.sort(key=lambda x: x.fitness, reverse=True)

#----------------------------------------------------------------------------------------------------------------------#
# Evolutionary algorithm
#----------------------------------------------------------------------------------------------------------------------#
generation = 0
best_fitness = population[0].fitness
solution = population[0].errors
pop_ave_fitness = []

# Loop until solution is found or after a certain number of iterations
while (generation < max_generations) and (solution > 0):

    generation += 1

    #------------------------------------------------------------------------------------------------------------------#
    # Parent Selection
    #------------------------------------------------------------------------------------------------------------------#
    
    # Uniform parent selection
    parents = selection.fitness_prop_selection(population, num_parents)

    # Randomly assign pairs of parents
    pairs = selection.random_parent_pairs(parents)
    
    #------------------------------------------------------------------------------------------------------------------#
    # Crossover 
    #------------------------------------------------------------------------------------------------------------------#
    
    offspring = []

    # Loop over all parent pairs
    for i in range(len(pairs)):

        # Check if crossover will occur for this pair    
        if (np.random.uniform(0, 1) <= cross_over_rate): 
            
            # partially-mapped crossover
            offspring += crossover.pmx(pairs[i][0], pairs[i][1])
            offspring += crossover.pmx(pairs[i][1], pairs[i][0])

        # If no crossover, just use these parents as offspring 
        else:
            offspring += [pairs[i][0], pairs[i][1]]

    # Keep only num_offspring
    offspring = [offspring[i] for i in range(num_offspring)]

    
    #------------------------------------------------------------------------------------------------------------------#
    # Mutation
    #------------------------------------------------------------------------------------------------------------------#
    # Loop over each offspring
    for i in range(len(offspring)):

        # Check if mutation will occur
        if (np.random.uniform(0, 1) <= mutation_rate): 

            # inversion mutation
            offspring[i] = mutation.inversion(offspring[i])


    #------------------------------------------------------------------------------------------------------------------#
    # Survival
    #------------------------------------------------------------------------------------------------------------------#

    # Increase age of all individuals in current generation
    for i in range(pop_size): population[i].increment_age() 

    # Replacement survival
    population = survival.replacement(population, offspring)

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

    # Check if solution found
    solution = population[0].errors

    #------------------------------------------------------------------------------------------------------------------#
    # Optional prints about generation
    #------------------------------------------------------------------------------------------------------------------#
    if prints:
        print('Generation: {:4d} Population Size: {:3d} '.format(generation, len(population)) +
              'Average Fitness: {:.3f} Best Phenotype: {} Age: {:3d} Fitness: {:.3f} Errors: {:2d}'.format(ave, 
                                                                              population[0].genotype, 
                                                                              population[0].age,
                                                                              population[0].fitness,
                                                                              population[0].errors))
        

#------------------------------------------------------------------------------------------------------------------#
# Optional plots
#------------------------------------------------------------------------------------------------------------------#


if plots:
    
    # Showing average fitness over generations
    plt.figure(1)
    plt.plot([i for i in range(generation)], pop_ave_fitness, color='b', linestyle='-', linewidth=2)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.ylabel('Population Average Fitness', fontsize=14)
    plt.xlabel('Generation', fontsize=14)
    plt.savefig('output/fitness_vs_generation.png', bbox_inches='tight', pad_inches=0)

    # Showing best solution on a grid
    plt.figure(2)
    grid = np.zeros((grid_size, grid_size))
    for i in range(grid_size): grid[population[0].genotype[i], i] = 1
    plt.imshow(grid)
    ax = plt.gca()
    ax.set_xticks(np.arange(-0.5, grid_size, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, grid_size, 1), minor=True)
    ax.grid(which='minor', color='k', linestyle='-', linewidth=2)
    plt.savefig('output/solution.png', bbox_inches='tight', pad_inches=0)

    # Show all
    plt.show()
    








