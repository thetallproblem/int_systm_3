import random


def f(x):  # min
    return x**2 + 4


# Начальная популяция
def create_init_pop(pop_size, chrom_len):
    initial_population = []
    for i in range(pop_size):
        chromosome = []
        for j in range(chrom_len):
            chromosome.append(random.randint(0, 1))
        initial_population.append(chromosome)

    return initial_population
