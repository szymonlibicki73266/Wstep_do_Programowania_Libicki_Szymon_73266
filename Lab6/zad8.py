import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 20, 30, 43, 55, 70, 90, 110]
plt.scatter(x, y)

plt.xlabel("Czas [s]")
plt.ylabel("Prędkość [km/h]")

plt.title("Prędkość chwilowa pojazdu")

plt.show()