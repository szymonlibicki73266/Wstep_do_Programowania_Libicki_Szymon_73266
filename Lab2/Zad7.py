imie = input("Podaj imię: ")
print("Witaj, " + imie)

wiek = int(input("Podaj wiek: "))
print("Twój wiek to:", wiek)

imienazwisko = input("Podaj imię i nazwisko: ")
print(imienazwisko[0] + imienazwisko[imienazwisko.index(" ") + 1])

lancuch = input("Podaj łańcuch znaków: ")
for i in range(5):
    print(lancuch)

lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
luncuch3 = (lancuch1 + lancuch2)
print(luncuch3)

lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
srodek1 = len(lancuch1) / 2
srodek2 = len(lancuch2) / 2
lancuch3 = lancuch1[:srodek1] + lancuch2[srodek2:]
print(luncuch3)