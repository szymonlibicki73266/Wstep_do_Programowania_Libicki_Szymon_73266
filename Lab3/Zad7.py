import random
a = random.randint(3, 7)
b = random.randint(3, 7)
X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))
print("Zbiór X:", X)
print("Zbiór Y:", Y)

print("Czy zbiór X zawiera liczbę 5?", 5 in X)

print("Czy zbiór X jest podzbiorem zbioru Y?", X.issubset(Y))

print("Czy zbiór Y jest podzbiorem zbioru X?", Y.issubset(X))

print("Suma zbiorów X oraz Y:", X.union(Y))

print("Różnica zbiorów X oraz Y:", X.difference(Y))

print("Różnica zbiorów Y oraz X:", Y.difference(X))

print("Iloczyn zbiorów X oraz Y:", X.intersection(Y))

print("Wartość najwyższego elementu w obu zbiorach:", max(X.union(Y)))

if X:
    element = X.pop()
    Y.add(element)
    print(f"Usunięto element {element} ze zbioru X i dodano do zbioru Y.")
    print("Zbiór X po usunięciu elementu:", X)
    print("Zbiór Y po dodaniu elementu:", Y)

Y.update(X)
print("Zbiór Y po skopiowaniu elementów ze zbioru X:", Y)

X.clear()
Y.clear()
print("Zbiór X po wyczyszczeniu:", X)
print("Zbiór Y po wyczyszczeniu:", Y)