import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Beispiel-Daten erstellen basierend auf den Informationen
data = {
    'Category': [
        'Spiritualität', 'Lebensbalance', 'Ökologische Nachhaltigkeit', 
        'Finanzieller Wohlstand', 'Beziehungen', 'Interesse an Luxusgütern',
        'Kaufmotive: Qualität', 'Kaufmotive: Komfort', 'Markenpräferenzen: Porsche', 
        'Markenpräferenzen: Ferrari', 'Markenpräferenzen: Lamborghini',
        'Nutzung öffentlicher Verkehrsmittel', 'Autonutzung', 'Flugreisen', 
        'Fahrradnutzung', 'Car-Sharing', 'Transportkriterien: Bequemlichkeit', 
        'Transportkriterien: Praktikabilität', 'Porsche und Spiritualität: Ja',
        'Porsche und Spiritualität: Nein'
    ],
    'Percentage': [
        20, 81, 8, 43, 86, 28, 66, 62, 53, 53, 53, 38, 45, 23, 15, 5, 62, 68, 19, 81
    ]
}

df = pd.DataFrame(data)

# Set style for the plots
sns.set(style="whitegrid")

# Creating the plots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Werte und Überzeugungen
values_beliefs = df.iloc[0:5]
sns.barplot(ax=axes[0, 0], x='Percentage', y='Category', data=values_beliefs, palette="viridis")
axes[0, 0].set_title('Werte und Überzeugungen')
axes[0, 0].set_xlabel('Prozent')
axes[0, 0].set_ylabel('')

# Plot 2: Luxuskaufentscheidungen
luxury_purchase = df.iloc[5:11]
sns.barplot(ax=axes[0, 1], x='Percentage', y='Category', data=luxury_purchase, palette="plasma")
axes[0, 1].set_title('Luxuskaufentscheidungen')
axes[0, 1].set_xlabel('Prozent')
axes[0, 1].set_ylabel('')

# Plot 3: Mobilitätspräferenzen
mobility_preferences = df.iloc[11:18]
sns.barplot(ax=axes[1, 0], x='Percentage', y='Category', data=mobility_preferences, palette="cubehelix")
axes[1, 0].set_title('Mobilitätspräferenzen')
axes[1, 0].set_xlabel('Prozent')
axes[1, 0].set_ylabel('')

# Plot 4: Verbindung zwischen Porsche und Spiritualität
porsche_spirituality = df.iloc[18:20]
sns.barplot(ax=axes[1, 1], x='Percentage', y='Category', data=porsche_spirituality, palette="magma")
axes[1, 1].set_title('Verbindung zwischen Porsche und Spiritualität')
axes[1, 1].set_xlabel('Prozent')
axes[1, 1].set_ylabel('')

plt.tight_layout()

# Grafiken speichern
plt.savefig('umfrage_grafiken.png')

plt.show()
