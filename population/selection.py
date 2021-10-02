import numpy as np

def tournament(population, n, k):
    '''
    Function for selecting parents

    This function selects the best n out of k randomly selected individuals to be parents in the mating pool.
    '''

    # Pick candidate parents (chance the same parent could be selected multiple times)
    parent_cand_idxs = np.random.randint(len(population), size=k)
    parent_candidates = [population[i] for i in parent_cand_idxs]

    # Sort the candidates by fitness
    parent_candidates.sort(key=lambda x: x.fitness)

    # Keep only best parents
    parents = [parent_candidates[i] for i in range(n)]

    return parents 


def fitness_prop_selection(population, n):

    # Compute probability to be selected
    p_fps = np.array([])
    total_f = 0
    for i in range(len(population)):
        p_fps = np.append(p_fps, population[i].fitness)
        total_f += population[i].fitness
    p_fps = p_fps / total_f

    # Roulette-Wheel select each parent based on probability
    parents = []
    for i in range(n):
        r = np.random.uniform(0, 1) # Equal chance for any numver between [0,1)
        idx = 0
        ai = p_fps[0]
        while (ai < r): 
            idx += 1
            ai += p_fps[idx]
        parents.append(population[idx])

    return parents


def random_parent_pairs(parents):
    '''
    This function randomly generates unique pairs of parents.
    '''
    
    def remove_random(parents):
        '''
        Helper function which removes one random element from the list.
        '''
        idx = np.random.randint(len(parents))
        return parents.pop(idx)
    
    pairs = []
    while parents:
        p1 = remove_random(parents)
        p2 = remove_random(parents)
        pairs.append([p1, p2])

    return pairs




