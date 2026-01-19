import pandas as pd

data = {
    "Nr_albumu": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Ocena": [4.5, 3.0, 5.0, 4.0, 2.5],
    "WiekS": [22, 21, 24, 23, 25]
}

df = pd.DataFrame(data).set_index("Nr_albumu")

# print(df)

### A)
print("\n---- OCENA > 4")
print(
    df[df["Ocena"]>4]
)

### B)
print("\n---- SORTOWANIE WIEK")
print(
    df.sort_values("WiekS")
)

### C)
print("\n---- Grupowanie wiek")
print(
    df.groupby("Ocena")
    .agg(Średnia=("WiekS", "mean"))
)

### D)
df.to_csv("zad5.csv")

df2 = pd.read_csv("zad5.csv").set_index("Nr_albumu")


print("\n---- STARE")
print(df)

print("\n---- PLIK CSV")
print(df2)

### E)
df.loc[6] = {"Imię": "Marek", "Nazwisko": "Nowak", "Ocena": 4.0, "WiekS": 25}

print("\n---- NOWY STUDENT")
print(df)

### H)
print("\n---- UNIKALNE WARTOŚCI")
print(
    df["Ocena"].unique()
)

### I)
print("\n---- ILE OSÓB MA 5?")
print(
    len(df[df["Ocena"]==4])
)

