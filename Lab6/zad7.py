import matplotlib.pyplot as plt

kategorie = ['Smartfony', 'Tablety', 'Laptopy', 'Komputery']
wartosci = [1524, 327, 1200, 423]
plt.pie(wartosci, labels=kategorie,
autopct='%1.f%%', startangle=90,
colors=['orange', 'seagreen', 'teal',
'lightcoral'])
plt.title('Procenty sprzedaży w danych kategoriach')
plt.show()