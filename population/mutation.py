import numpy as np
from . import phenotype

def mutate(offspring, grid_size):

    # Random indexes to swap
    swap1 = np.random.randint(grid_size)
    swap2 = np.random.randint(grid_size)

    # Pull the genotype, swap
    genotype = offspring.genotype
    genotype[swap1],  genotype[swap2] = genotype[swap2], genotype[swap1]

    # Return new mutated offspring to replace 
    return phenotype.Phenotype(genotype)