import matplotlib.pyplot as plt


oceny = [3, 4, 5, 2, 3, 4, 4.5, 3.5, 5, 2, 3, 4, 3, 3.5, 4.5, 5, 2, 3, 4, 3]
bins = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]

plt.hist(oceny, bins=bins, edgecolor='black', align='left', color='skyblue')

plt.title('Rozkład ocen studentów')
plt.xlabel('Ocena')
plt.ylabel('Liczba studentów')

plt.xticks([2, 3, 3.5, 4, 4.5, 5])

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()