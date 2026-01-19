import numpy as np

macierz = np.zeros((5, 5))

macierz[0, :] = 1
macierz[-1, :] = 1
macierz[:, 0] = 1
macierz[:, -1] = 1

def zamien_wartosci(m):
    return np.where(m == 0, 1, 0)

macierz_zamieniona = zamien_wartosci(macierz)

print("< Macierz z ramką:\n", macierz)
print("\n< Macierz po zamianie:\n", macierz_zamieniona)