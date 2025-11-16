import string
lista_znakow = list(string.ascii_lowercase)
zdanie = input("Podaj zdanie: ").strip().lower()
unikalne_litery = sorted(set([litera for litera in zdanie if litera.isalpha()]))
print("Występujące litery w kolejności alfabetycznej:", ''.join(unikalne_litery))
brakujace_litery = [litera for litera in lista_znakow if litera not in unikalne_litery]
print("Brakujące litery alfabetu:", ''.join(brakujace_litery))