import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Daten für die Korrelationen
data_correlation = {
    'Correlation Level': [
        'High (0.5 and higher)',
        'High (0.5 and higher)',
        'High (0.5 and higher)',
        'Moderate (0.3 to 0.5)',
        'Moderate (0.3 to 0.5)',
        'Low (below 0.3)',
        'Low (below 0.3)'
    ],
    'Factor': [
        'Quality',
        'Performance',
        'Brand Image',
        'Technology',
        'Design',
        'Comfort',
        'Customer Service'
    ]
}

# Erstellen des DataFrames
df_correlation = pd.DataFrame(data_correlation)

# Erstellen der Grafik
plt.figure(figsize=(10, 6))
sns.barplot(x='Correlation Level', y='Factor', data=df_correlation, palette="viridis")
plt.title('Correlation between Porsche and Spirituality and Other Factors', fontsize=16)
plt.xlabel('Correlation Level', fontsize=14)
plt.ylabel('Factor', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x')

# Grafik anzeigen
plt.show()
