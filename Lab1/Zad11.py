try:
    a = int(input("Podaj liczbę całkowitą a: ").strip())
    b = int(input("Podaj liczbę całkowitą b: ").strip())
    c = int(input("Podaj liczbę całkowitą c: ").strip())
except ValueError:
    print("Błędne dane wejściowe. Proszę podać liczby całkowite.")
else:  
    delta = b*b - 4*a*c
    if delta > 0:    
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        print("Równanie ma dwa pierwiastki rzeczywiste: x1 =", x1, ", x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Równanie ma jeden podwójny pierwiastek rzeczywisty: x =", x)
    else:
        print("Równanie nie ma pierwiastków rzeczywistych.")