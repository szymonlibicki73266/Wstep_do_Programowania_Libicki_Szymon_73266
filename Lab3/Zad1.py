list = ["Szymon", "Magda", "Ania", "Kasia"]
list.sort()

list.append("Ola")
list.append("Zosia")

imie = list.pop()
print(imie)

list.insert(3, "Ola")

list.reverse()
list = list * 2
print(list)