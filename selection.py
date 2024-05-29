import random


# Вероятность скрещивания для особи
def p(population_fitness):
    fitness_prob = []
    for i in range(len(population_fitness)):
        prob = population_fitness[i] / sum(population_fitness)
        fitness_prob.append(prob)

    return fitness_prob


#Рулеточная селекция
def roulette_wheel_pop(population, probabilities, number):
    chosen = []
    for n in range(number):
        r = random.random()
        prob_circle = 0

        for i in range(len(probabilities)):
            prob_circle += probabilities[i]
            if r <= prob_circle:
                chosen.append(population[i])
                break

    return chosen


