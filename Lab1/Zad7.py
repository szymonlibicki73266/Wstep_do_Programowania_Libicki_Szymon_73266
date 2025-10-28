import random

cenapaliwa = float(6.5)
losowatrasa = int(random.randint(100,2000))
sredniespalanie = float(input("Podaj srednie spalanie:"))

szacowanezuzycie = (losowatrasa*100)*sredniespalanie
szacowanykosztpaliwa = szacowanezuzycie*cenapaliwa

print("Dla trasy",losowatrasa,"szacowane zuzycie paliwa to",szacowanezuzycie,"a szacowany koszt to", szacowanykosztpaliwa)

#Liczby zwracane są pseudoloswe są "ustalone" ze względy na zdefiniowany seed co oznacza że są one przewidywalne co przeczy samej definicji losowości