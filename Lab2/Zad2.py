
wiersze = int(input("Podaj liczbę wierszy: "))
for i in range(wiersze):
    for j in range(3):
        print("*", end=" ")
    print()

wiersze = int(input("Podaj liczbę wierszy: "))
for i in range(1, wiersze + 1):
    for j in range(i):
        print("*", end=" ")
    print()

wiersze = int(input("Podaj liczbę wierszy: "))
for i in range(1, wiersze + 1):
    for j in range(wiersze - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()