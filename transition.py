def decode_chrom(chromosome):
    n = len(chromosome)
    decimal_val = 0
    for i in range(n):
        decimal_val += chromosome[i] * (2 ** (n-i-1))

    x = decimal_val / (2**n - 1) * 0.31
    return x


def get_uniq_individual(population):
    new_population = []
    for elem in population:
        if elem not in new_population:
            new_population.append(elem)

    return new_population
