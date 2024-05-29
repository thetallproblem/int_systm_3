from genetic_alg import genetic_alg
from start_value import f
import matplotlib.pyplot as plt
import numpy as np

length_pop = int(input("Введите длину популяции: "))
chrom_len = int(input("Введите длину хромосомы: "))
pc = float(input("Введите вероятность скрещивания: "))
iterations = int(input("Введите число поколений: "))

result_x, result_y = genetic_alg(length_pop, chrom_len, pc, iterations)

x_plt = np.arange(-10, 10, 0.5)
f_plt = [f(x) for x in x_plt]

plt.grid(True)

plt.plot(x_plt, f_plt)
plt.scatter(result_x, result_y, c='red')

plt.show()
