import pandas as pd

data = {
    'Id': [1,2,3,4,5],
    'Imię': ['Anna', 'Jan', 'Katarzyna','Tomasz','Michał'],
    'Nazwisko': ['Kowalska', "Nowak", 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    "Stanowisko": ['Manager', 'Programista', 'Konsultant', 'Programista','Manager'],
    'Wiek': [35,28,40,30,45],
    'Pensja': [8000,4500,6000,5500,7000]
}

df = pd.DataFrame(data).set_index("Id")

### A)
print("\n< Pracownicy którzy zarabiają więcej niż 5000 PLN")
print(df["Imię"][df["Pensja"] > 5000].values)

### B)
print("\n---- SORTUJ WIEK")
print(df.sort_values("Wiek"))

### C)
print("\n---- ŚREDNIA NA STANOWISKO")
print(df.groupby("Stanowisko").agg(Średnia=("Pensja", "mean")))

### D)
print("\n---- STARA ")
zmiany = {
    'Id': [2, 4],
    "Stanowisko": ["Senior Programista", "Senior Programista"],
}

df_zmiany = pd.DataFrame(zmiany).set_index("Id")

print(df)

df.update(df_zmiany)

print("\n---- NOWA")
print(df)

### E)
df.to_csv("zad4.csv")

### F)
df2 = pd.read_csv("zad4.csv").set_index("Id")

print("\n---- WCZYTANE Z PLIKU")
print(df2)
