rachunki = {"styczeń": 120.50, "luty": 135.75, "marzec": 110.20, "kwiecień": 145.00, "maj": 95.40}
maksymalna = max(rachunki.values())
minimalna = min(rachunki.values())
suma = sum(rachunki.values())
srednia = suma / len(rachunki)
ostatni_miesiac = list(rachunki.values())[-1]
print(f"Wartość maksymalna: {maksymalna:.2f} zł")
print(f"Wartość minimalna: {minimalna:.2f} zł")
print(f"Suma: {suma:.2f} zł")
print(f"Wartość średnia: {srednia:.2f} zł")
if ostatni_miesiac > srednia:
    print("Trzeba zacisnąć pasa.")
else:
    print("Wszystko okay.")