def srednia_z_listy(liczby):
    if not liczby:
        return 0
    return sum(liczby) / len(liczby)

lista_liczb = [1, 2, 3, 4, 5]
print(f"Średnia z listy {lista_liczb} wynosi: {srednia_z_listy(lista_liczb):.2f}")