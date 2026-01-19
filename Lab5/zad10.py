losowe = (4,2,1,5,6,3,2,7,5,3)

wynik = 1

for i in losowe:
    wynik*=i

wynik = wynik**(1/len(losowe))

print(f" Średnia geometryczna krotki {losowe}\n"
      f" Wynosi: {wynik}")