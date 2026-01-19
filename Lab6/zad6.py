import matplotlib.pyplot as plt

kategorie = ['Smartfony', 'Tablety', 'Laptopy', 'Komputery']
wartosci = [1524, 327, 1200, 423]
plt.bar(kategorie, wartosci)
plt.title("Ilość sprzedanych rzeczy danej kategorii")
plt.show()