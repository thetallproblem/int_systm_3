from start_value import f
from transition import decode_chrom


#Расчёт фитнес функции
def fitness_fun(initial_population):
    population_fitness = []
    for chromosome in initial_population:
        fitness = f(decode_chrom(chromosome))
        population_fitness.append(fitness)

    return population_fitness
