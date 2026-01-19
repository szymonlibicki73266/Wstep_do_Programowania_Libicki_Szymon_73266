import numpy as np

macierz = np.random.rand(5, 5)

max_element = np.max(macierz)
min_element = np.min(macierz)

max_wiersze = np.max(macierz, axis=1)
max_kolumny = np.max(macierz, axis=0)

suma_wierszy = np.sum(macierz, axis=1)

print("< Macierz:\n", macierz)
print("\n< Największy element:", max_element)
print("< Najmniejszy element:", min_element)
print("< Największe w każdym wierszu:", max_wiersze)
print("< Największe w każdej kolumnie:", max_kolumny)
print("< Suma wartości w wierszach:", suma_wierszy)