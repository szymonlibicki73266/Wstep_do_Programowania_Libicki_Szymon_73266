while True:
    try:
        x = int(input("Podaj liczbę rzeczywistą (ujemną aby zakończyć): "))
    except ValueError:
        print("Błędne dane wejściowe. Proszę podać liczbę rzeczywistą.")
        continue
    
    if x < 0:
        break