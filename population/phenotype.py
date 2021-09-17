import numpy as np

'''
Basic solution object to the 8-Queens problem. Each Phenotype has an associated genotype which representes the solution 
as a vector, and an associated fitness. 
'''
class Phenotype:

    def __init__(self, genotype):
        self.genotype = genotype
        self.fitness = self._eval_fitness()


    def _eval_fitness(self):
        fitness = 0

        # Loop over every pair of Queen's
        for i in range(len(self.genotype)-1):
            for j in range(i+1, len(self.genotype)):

                # Check for same row
                if self.genotype[i] == self.genotype[j]:
                    fitness += 1

                # Check for same diagonal 
                if abs(j - i) == abs(self.genotype[j] - self.genotype[i]):
                    fitness += 1
        
        return fitness