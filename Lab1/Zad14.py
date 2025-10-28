nazwapliku = input("Podaj nazwę pliku: ").strip()
if nazwapliku.endswith('.xls') or nazwapliku.endswith('.xlsx'):
    print("Plik jest arkuszem Excel.")
else:
    print("Plik nie jest arkuszem Excel.")
    
# Metoda endswith() sprawdza czy na końcu jest określona końcówka.