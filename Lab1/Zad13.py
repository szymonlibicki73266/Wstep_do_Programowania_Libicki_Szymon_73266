def dodawanie(x, y):
    return x + y    
def odejmowanie(x, y):
    return x - y
def mnozenie(x, y):
    return x * y
def dzielenie(x, y):
    if y == 0:
        return "Nie można dzielić przez zero."
    return x / y
print("Wybierz operację:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
wybor = input("Wpisz numer operacji (1/2/3/4): ").strip()
try:
    num1 = float(input("Podaj pierwszą liczbę: ").strip())
    num2 = float(input("Podaj drugą liczbę: ").strip())
except ValueError:
    print("Błędne dane wejściowe. Proszę podać liczby.")
else:
    if wybor == '1':
        print(num1, "+", num2, "=", dodawanie(num1, num2))
    elif wybor == '2':
        print(num1, "-", num2, "=", odejmowanie(num1, num2))
    elif wybor == '3':
        print(num1, "*", num2, "=", mnozenie(num1, num2))
    elif wybor == '4':
        print(num1, "/", num2, "=", dzielenie(num1, num2))
    else:
        print("Błędny wybór operacji.")

# W Pythonie nie ma bezpośredniego odpowiednika instrukcji switch znanej z innych języków programowania. Zamiast tego używamy wielokrotnych instrukcji elif z zdefiniowanymi funkcjami