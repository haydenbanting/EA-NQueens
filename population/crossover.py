import numpy as np
from . import phenotype

def crossover(parent1, parent2, grid_size):

    # Simple cross-over, should be fixed to keep "good" parts

    # Random point to split the parent's geno
    split = np.random.randint(1, grid_size)

    # Create combination of parent's geno
    genotype1 = np.concatenate( (parent1.genotype[0:split], parent2.genotype[split:]), axis=0 )
    genotype2 = np.concatenate( (parent2.genotype[0:split], parent1.genotype[split:]), axis=0 )

    # New off spring 
    offspring1 = phenotype.Phenotype(genotype1)
    offspring2 = phenotype.Phenotype(genotype2)

    return [offspring1, offspring2]