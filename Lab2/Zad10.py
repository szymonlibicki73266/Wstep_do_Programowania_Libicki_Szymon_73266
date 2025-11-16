try:
    a = int(input("Podaj pierwszą liczbę całkowitą: ").strip())
    b = int(input("Podaj drugą liczbę całkowitą: ").strip())
except ValueError:
    print("Błędne dane wejściowe. Proszę podać liczby całkowite.")
else:
    start = min(a, b)
    end = max(a, b)
    while start <= end:
        print(start)
        start += 1