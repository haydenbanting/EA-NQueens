import random
import numpy as np
from . import phenotype

def crossover(parent1, parent2, grid_size):

    assert(len(parent1.genotype) == len(parent2.genotype))

    # Random point to split the parent's geno
    split = np.random.randint(1, grid_size)

    # Create combination of parent's geno
    genotype1 = np.concatenate( (parent1.genotype[0:split], parent2.genotype[split:]), axis=0 )
    genotype2 = np.concatenate( (parent2.genotype[0:split], parent1.genotype[split:]), axis=0 )

    # New off spring 
    offspring1 = phenotype.Phenotype(genotype1)
    offspring2 = phenotype.Phenotype(genotype2)

    return [offspring1, offspring2]


def inversion(parent):

    # Pick two unique random values, so at least 1 value is inverted, put in correct order
    edges = np.sort(np.random.choice(range(0, len(parent.genotype)+1), 2, replace=False))

    # Assign the offsrping the parent
    geno = parent.genotype

    # Reverse the the random section
    geno[edges[0]:edges[1]] = geno[edges[0]:edges[1]][::-1]

    # Create new offspring object
    offspring = phenotype.Phenotype(geno)

    return  [offspring]