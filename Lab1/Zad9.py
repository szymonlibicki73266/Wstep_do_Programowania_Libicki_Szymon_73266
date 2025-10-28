try:
    wiek = int(input("Podaj swoj wiek: "))
except ValueError:
    print("To nie jest wiek")
else:
    if wiek >= 18:
        try:
            student = input("Czy jestes studentem? (tak/nie): ")
        except ValueError:
            print("Niepoprawna odpowiedz")
            cenabiletu = None
        else:
            if student == "tak":
                cenabiletu = 15
            elif student == "nie":
                cenabiletu = 20
            else:
                print("Niepoprawna odpowiedz")
                cenabiletu = None
    elif wiek >= 4 and wiek < 18:
        cenabiletu = 10
    else:   
        cenabiletu = 0
    if cenabiletu is not None:
        print("Cena biletu wynosi:", cenabiletu)