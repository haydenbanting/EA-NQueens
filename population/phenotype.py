import numpy as np

'''
Basic solution object to the 8-Queens problem. Each Phenotype has an associated genotype which representes the solution 
as a vector, and an associated fitness. 
'''
class Phenotype:

    def __init__(self, genotype):
        self.age = 0
        self.genotype = genotype
        self.fitness, self.errors = self._eval_fitness()
        

    def increment_age(self):
        self.age += 1
             
    def _eval_fitness(self):
        errors = 0
        genotype = self.genotype

        # Compute max number of errors (every pair of Queens in check)
        max_errors = len(genotype)* (len(genotype)-1) / 2
        
        # Loop over every pair of Queen's
        for i in range(len(genotype)-1):
            for j in range(i+1, len(genotype)): 

                # Check for same row (should never occur with good initialization)
                if genotype[i] == genotype[j]:
                    errors += 1
                    
                # Check for same diagonal 
                if abs(i - j) == np.abs(genotype[i] - genotype[j]): 
                    errors += 1
                    
        return (max_errors - errors) / max_errors, errors