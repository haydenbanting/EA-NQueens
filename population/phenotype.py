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
        genotype = self.genotype
        
        # Loop over every pair of Queen's
        for i in range(len(genotype)-1):
            for j in range(i+1, len(genotype)): 

                #print(type(self.genotype))
                #print(type(self.genotype[0]))
                ##print(type(i))
                #assert(0==1)

                # Check for same row (should never occur with good initialization)
                if genotype[i] == genotype[j]:
                    fitness += 1
                    
                # Check for same diagonal 
                ### ISSUE HERE
                if abs(i - j) == np.abs(genotype[i] - genotype[j]): 
                    fitness += 1
                    
        return fitness