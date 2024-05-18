import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Datei einlesen
file_path = '"C:\Users\mihae\Downloads\Porsche Survey Results.xls"'  # Ersetze dies durch den tatsächlichen Pfad zu deiner Datei
df = pd.read_excel(file_path)

# Fehlende Daten bereinigen (Beispiel: Ersetze -77 und -99 durch NaN)
df = df.replace([-77, -99], pd.NA)

# Deskriptive Statistiken
print(df.describe())

# Korrelationen berechnen
correlation_matrix = df.corr()
print(correlation_matrix)

# Heatmap der Korrelationen
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
