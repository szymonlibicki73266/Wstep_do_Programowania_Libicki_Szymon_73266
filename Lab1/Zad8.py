try:
    wiek = int(input("Podaj swoj wiek: ").strip())
except ValueError:
    print("To nie jest wiek")
else:
    if wiek >= 18:
        print("jestes pelnoletni")
    else:
        print("nie jestes pelnoletni")