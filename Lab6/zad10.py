import numpy as np

wagi = np.array([128, 64, 32, 16, 8, 4, 2, 1])
liczba_bin = np.random.randint(0, 2, size=8)

def wartosc_liczby_bin(wagi, liczba_bin):
    return np.sum(wagi * liczba_bin)

wynik = wartosc_liczby_bin(wagi, liczba_bin)

print(wynik)