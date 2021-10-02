import random
import numpy as np
from . import phenotype

def cut_and_crossfill(parent1, parent2):

    # Sanity check
    assert(len(parent1.genotype) == len(parent2.genotype))

    # Random point to split the parent's geno
    split = np.random.randint(1, len(parent1.genotype))

    # Create combination of parent's geno
    genotype1 = np.concatenate( (parent1.genotype[0:split], parent2.genotype[split:]), axis=0 )
    genotype2 = np.concatenate( (parent2.genotype[0:split], parent1.genotype[split:]), axis=0 )

    # New off spring 
    offspring1 = phenotype.Phenotype(genotype1)
    offspring2 = phenotype.Phenotype(genotype2)

    return [offspring1, offspring2]


def pmx(parent1, parent2):

    # Sanity check
    assert(len(parent1.genotype) == len(parent2.genotype))

    # Pull parents genotypes
    p1 = parent1.genotype
    p2 = parent2.genotype

    # Initialize offspring Geno with invalid values ("empty spots")
    geno = np.zeros(len(p1), dtype=int)-1
    
    # Pick two unique random values, so at least 1 value is inverted, put in correct order
    edges = np.sort(np.random.choice(range(0, len(parent1.genotype)+1), 2, replace=False))

    # Copy selection from parent 1 to geno
    geno[edges[0]:edges[1]] = p1[edges[0]:edges[1]]

    # Loop over elements in p2 starting from first cross over point
    for i in np.roll(p2, len(p2)-edges[0]):

        # If this value is not already in offspring, add it
        if i not in geno:
            
            # Get index of i in p2
            idx = np.where(p2 == i)

            # Check if this spot in offpsring is empty
            val = geno[idx]

            # Keep searching
            while (val != -1):

                # Index of val in p2
                idx = np.where(p2 == val)

                # Check the value in the offspring at idx
                val = geno[idx]

            # Add i to offspring
            geno[idx] = i

    # New offspring
    offspring =  phenotype.Phenotype(geno)
    return [offspring]