import pandas as pd

sheet = pd.read_excel("C:\\Users\\bglowacz\\Documents\\Zeszyt1.xlsx")
column_a = sheet[1:3]

# wybierz potrzebne kolumny po indeksach
columns_to_keep = [0, 2]
df = sheet.iloc[:, columns_to_keep]

# lub wybierz potrzebne kolumny po nazwach
# columns_to_keep = ['A', 'B', 'C']
# df = sheet[columns_to_keep]

# wyświetl wynik
print(df)
