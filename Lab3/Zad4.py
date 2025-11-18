import random
lista = []
slowo = ""
try:
    n = int(input("Podaj liczbę całkowita n: "))
    x = int(input("Podaj liczbę całkowitą x: "))
except ValueError:
    print("Podaj tylko liczby całkowite!")
else:
    for i in range(n):
        for j in range(random.randint(1, x)):
            slowo += (chr(random.randint(97, 122)))
        lista.append(slowo)
        slowo = ""
print(lista)
        
krotka = tuple(lista)
print(krotka)

ilosc_znakow = 0
for element in krotka:
    ilosc_znakow += len(element)
print("Ilość znaków w krotce:", ilosc_znakow)

ilosc_k = 0
for element in krotka:
    ilosc_k += element.count('k')
print("Ilość liter k w krotce:", ilosc_k)

ilosc_kt = 0
for element in krotka:
    ilosc_kt += element.count('kt')
print("Ilość wystąpień ciągu 'kt' w krotce:", ilosc_kt)

s = int(input("Podaj długość szukanych ciągów znaków: "))
count = 0
for element in krotka:
    if len(element) > s:
        count += 1
print("Ilość ciągów znaków dłuższych niż", s, "w krotce:", count)