import numpy as np

macierz = np.random.randint(0, 50, size=(5, 5))

elementy_wieksze_20 = macierz[macierz > 20]
liczba_elementow = elementy_wieksze_20.size
srednia = np.mean(macierz)

print("< Macierz:\n", macierz)
print("< Liczba elementów większych niż 20:", liczba_elementow)
print("< Średnia całej macierzy:", srednia)