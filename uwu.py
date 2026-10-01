import pandas as pd

df20 = pd.read_csv('datos/2020.csv')
df21 = pd.read_csv('datos/2021.csv')
df22 = pd.read_csv('datos/2022.csv')
df23 = pd.read_csv('datos/2023.csv')
df24 = pd.read_csv('datos/2024.csv')
df25 = pd.read_csv('datos/2025.csv')
df26 = pd.read_csv('datos/2026.csv')


print(df20.head())
print(df21.head())
print(df22.head())
print(df23.head())
print(df24.head())
print(df25.head())
print(df26.head())

for column in df20.columns:
    print(f"Column: {column}")
    print(f"2020: {df20[column].dtype}, 2021: {df21[column].dtype}, 2022: {df22[column].dtype}, 2023: {df23[column].dtype}, 2024: {df24[column].dtype}, 2025: {df25[column].dtype}, 2026: {df26[column].dtype}")
    print()