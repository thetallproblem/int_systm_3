import random


def crossover(parent_1, parent_2, crossover_point):
    return parent_1[:crossover_point] + parent_2[crossover_point:]


def mutation(individual):
    pm = 1 / len(individual)

    for i in range(len(individual)):
        if random.random() < pm:
            individual[i] = 1 - individual[i]

    return individual


def population_crossover(population, pc):
    new_pop = []
    for i in range(0, len(population), 2):
        if pc > random.random():
            crossover_point = random.randint(1, len(population[i]) - 1)
            new_pop.append(mutation(crossover(population[i], population[i + 1], crossover_point)))
            new_pop.append(mutation(crossover(population[i + 1], population[i], crossover_point)))
        else:
            new_pop.append(population[i])
            new_pop.append(population[i + 1])

    return new_pop
