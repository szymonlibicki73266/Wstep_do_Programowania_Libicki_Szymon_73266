try:
    x1 = int(input("Podaj liczbę całkowitą dla przykładu a: ").strip())
    x2 = int(input("Podaj liczbę całkowitą dla przykładu b: ").strip())
    x3 = int(input("Podaj liczbę całkowitą dla przykładu c: ").strip())
except ValueError:
    print("Błędne dane wejściowe. Proszę podać liczby całkowite.")
else:
    #a
    if x1 > 0:
        a = 2 * x1
    elif x1 == 0:
        a = 0
    else:
        a = -3 *x1
    print("Wynik dla przykładu a:", a)
    #b
    if x2 >= 1:
        b = x2^2
    else:
        b = x2
    print("Wynik dla przykładu b:", b)
    #c
    if x3 > 2:
        c = 2 + x3
    elif x3 == 2:
        c = 8
    else:
        c = x3 - 4
    print("Wynik dla przykładu c:", c)