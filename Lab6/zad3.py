import pandas as pd

df = pd.read_csv(
    'demografia.csv',
    na_values='.'
)

# Rok, w którym jest największa wartość
rok = df.iloc[:,1:].max().idxmax()

# Wynik przyrostu
przyrost = df[rok].max()

# W jakim kraju
kraj = df["KRAJE"][df[rok].idxmax()]

print(f"< Największy przyrost był w roku {rok},"
      f"\ni wynosił on {przyrost},"
      f"\nw kraju {kraj}")

