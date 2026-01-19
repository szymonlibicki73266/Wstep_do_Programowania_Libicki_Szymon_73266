import pandas as pd

df = pd.read_csv(
    'demografia.csv',
    na_values='.')

print(df[['KRAJE','2022']])


MAX_INDEX = df['2022'].idxmax()
kraj = df['KRAJE'][MAX_INDEX].strip()
liczba = df['2022'][MAX_INDEX]

print(f"> Kraj w którym odnotowano największy przyrost ludności\n"
      f"w 2022 to {kraj} i wynosi {liczba}")