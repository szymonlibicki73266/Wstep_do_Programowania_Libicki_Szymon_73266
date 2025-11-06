n = int(input("Podaj liczbę naturalną n: "))

silniaodn = 1
for i in range(1, n + 1):
    silniaodn *= i
print(silniaodn)