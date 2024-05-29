from start_value import create_init_pop, f
from fitness_fun import fitness_fun
from selection import p, roulette_wheel_pop
from transition import get_uniq_individual, decode_chrom
from crossover_mutation import population_crossover


def print_result(population, j):
    print("Последняя популяция №{}: ".format(j))
    print(population)

    f_population = []

    for i in range(len(population)):
        print("Целевая функция y=x^2+4 особи #{} равна: {}".format(i + 1, f(population[i])))
        f_population.append(f(population[i]))

    min_ind = f_population.index(min(f_population))
    print("Точка минимума: [{}, {}]".format(population[min_ind], f_population[min_ind]))

    return population[min_ind], f_population[min_ind]


def genetic_alg(length_pop, chrom_size, pc, iteration):
    new_population = []
    result_population = create_init_pop(length_pop, chrom_size)

    print("Начальная популяция: [", end='')
    for i in range(len(result_population) - 1):
        print(decode_chrom(result_population[i]), end=', ')
    print(f"{decode_chrom(result_population[len(result_population) - 1])}]")

    population_fitness = fitness_fun(result_population)
    for i in range(len(result_population)):
        print("Приспособленность особи #{} равна: {}".format(i + 1, population_fitness[i]))

    fitness_prob = p(population_fitness)
    for i in range(len(population_fitness)):
        print("Вероятность скрещивания особи #{} равна: {}".format(i + 1, fitness_prob[i]))

    for j in range(iteration):
        population_fitness = fitness_fun(result_population)
        fitness_prob = p(population_fitness)

        population_for_crossover = roulette_wheel_pop(result_population, fitness_prob, length_pop)
        new_population = population_crossover(population_for_crossover, pc)
        population_for_crossover = get_uniq_individual(population_for_crossover)

    for i in range(len(new_population)):
        new_population[i] = decode_chrom(new_population[i])

    return print_result(new_population, iteration)
