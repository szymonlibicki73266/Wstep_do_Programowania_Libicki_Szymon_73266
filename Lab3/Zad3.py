import string
tekst = input("Podaj ciąg znaków: ").strip().lower()
tekst_czysty = ''.join([znak for znak in tekst if znak.isalnum()])
if tekst_czysty == tekst_czysty[::-1]:
    print("Podany ciąg znaków jest palindromem.")
else:
    print("Podany ciąg znaków nie jest palindromem.")