import numpy as np


def replacement(population, offspring):
    '''
    This function will replace lowest-fitness individuals in the population with the offspring. 
    '''
    # Remove worst indiviudals from population
    population = population[:len(population) - len(offspring)]

    # Add offspring 
    population += offspring

    # Sort the population again with new members
    population.sort(key=lambda x: x.fitness, reverse=True)

    return population


def fitness_prop_selection(population, offspring):
    '''
    This is similar to function in selection.py. Should make a generic roulette wheel routine to be shared between them.
    '''
    # Pool together population and offspring
    current_gen = population + offspring

    # Compute probability to be selected
    p_fps = np.array([])
    total_f = 0
    for i in range(len(current_gen)):
        p_fps = np.append(p_fps, current_gen[i].fitness)
        total_f += current_gen[i].fitness
    p_fps = p_fps / total_f

    # Roulette-Wheel to select next gen survivors (same number as in population)
    next_gen = []
    for i in range(len(population)):
        r = np.random.uniform(0, 1) # Equal chance for any numver between [0,1)
        idx = 0
        ai = p_fps[0]
        while (ai < r): 
            idx += 1
            ai += p_fps[idx]
        next_gen.append(current_gen[idx])

    return next_gen


