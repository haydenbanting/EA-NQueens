#----------------------------------------------------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt 
from population import phenotype
from population import crossover
from population import mutation
from population import selection

#----------------------------------------------------------------------------------------------------------------------#
# Parameters
#----------------------------------------------------------------------------------------------------------------------#
grid_size = 12              
pop_size = 100            
selection_size = 100         
num_parents = 20          
num_offspring = 10          
mutation_rate = 0.3         
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
# Random initialization
#population = [phenotype.Phenotype(np.random.randint(grid_size, size=grid_size)) for i in range(pop_size)]

# Improved initialization
population = [phenotype.Phenotype(np.random.permutation(np.arange(grid_size))) for i in range(pop_size)]

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

    #------------------------------------------------------------------------------------------------------------------#
    # Parent Selection
    #------------------------------------------------------------------------------------------------------------------#
    parents = selection.fitness_prop_selection(population, num_parents)

    # Randomly assign pairs of parents
    pairs = selection.random_parent_pairs(parents)
    
    #------------------------------------------------------------------------------------------------------------------#
    # Crossover 
    #------------------------------------------------------------------------------------------------------------------#
    
    # Simple Crossover
    offspring = []

    # Loop over all parent pairs
    for i in range(len(pairs)):

        # Check if cross-over will occur for this pair    
        if (np.random.uniform(0, 1) <= cross_over_rate): 
            offspring += crossover.crossover(pairs[i][0], pairs[i][1], grid_size)
            #crossover.inversion(pairs[i][0])

        # If no crossover, just use these parents as offspring 
        else:
            offspring += [pairs[i][0], pairs[i][1]]

    # Keep only num_offspring
    offspring = [offspring[i] for i in range(num_offspring)]

    
    # Inversion crossover - problems
    '''
    offspring = []
    for i in range(num_offspring):

        # select random parent
        idx = np.random.randint(len(parents))
        #parent = parents.pop(idx)
        parent = parents[idx]

        # Check if cross-over will occur for this pair    
        if (np.random.uniform(0, 1) <= cross_over_rate): 
            offspring += crossover.inversion(parent)

        # If no crossover, just use these parents as offspring 
        else:
            offspring += [parent]
        '''
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
    population += offspring
    population.sort(key=lambda x: x.fitness)
    population = population[:len(population) - len(offspring)]
    assert(len(population) == pop_size)
    '''
    # Add each offspring into population
    for i in range(len(offspring)):

        # Insert them into sorted population
        for j in range(len(population)):
            if (offspring[i].fitness < population[j].fitness):
                population.insert(j, offspring[i]) 
                break
            elif (j == len(population) - 1): # edge case (new best)
                population.insert(j, offspring[i])

    
    # Remove worst candidates in population
    population = population[:len(population) - len(offspring)]

    # Keeping population size contant each generation
    assert(len(population) == pop_size)
    '''
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
        print('Generation: {:4d} Population Size: {:3d} '.format(generation, len(population)) +
              'Average Fitness: {:.2f} Best Phenotype: {} Fitness: {}'.format(ave, 
                                                                              population[0].genotype, 
                                                                              population[0].fitness))
        

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
    








