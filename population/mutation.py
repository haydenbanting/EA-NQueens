import numpy as np
from . import phenotype

def swap(offspring):

    # Random indexes to swap
    swap1 = np.random.randint(len(offspring.genotype))
    swap2 = np.random.randint(len(offspring.genotype))

    # Pull the genotype, swap
    genotype = offspring.genotype
    genotype[swap1],  genotype[swap2] = genotype[swap2], genotype[swap1]

    # New offspring
    offspring = phenotype.Phenotype(genotype)

    # Return new mutated offspring to replace 
    return offspring


def inversion(offspring):

    # Pick two unique random values, so at least 1 value is inverted, put in correct order
    edges = np.sort(np.random.choice(range(0, len(offspring.genotype)+1), 2, replace=False))

    # Get the offspring geno
    geno = offspring.genotype

    # Reverse the the random section
    geno[edges[0]:edges[1]] = geno[edges[0]:edges[1]][::-1]

    # Create new offspring object
    offspring = phenotype.Phenotype(geno)

    return offspring