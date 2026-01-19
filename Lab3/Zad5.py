zakupy = {"chleb": 3.50, "mleko": 2.80, "jajka": 5.20, "masło": 4.10, "ser": 6.30, "jabłka": 4.00, "banany": 3.60, "kurczak": 12.50}
print("\nLista zakupów:")
for artykul, kwota in zakupy.items():
    print(f"{artykul}: {kwota:.2f} zł")
suma_wydatkow = sum(zakupy.values())
print(f"\nŁączne wydatki: {suma_wydatkow:.2f} zł")