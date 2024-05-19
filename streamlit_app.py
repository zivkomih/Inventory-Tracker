import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Stil für die Diagramme festlegen
sns.set(style="whitegrid")

# Farben definieren
colors = ["#EBD698", "#000000", "#B12B28"]

# Titel der App
st.title("Survey Results: Correlation between Porsche and Spirituality and Other Factors")

# Plot: Correlation Chart
st.subheader('Correlation Chart')
plt.figure(figsize=(10, 6))
sns.barplot(x='Correlation Level', y='Factor', data=df_correlation, palette=colors)
plt.title('Correlation between Porsche and Spirituality and Other Factors', fontsize=16)
plt.xlabel('Correlation Level', fontsize=14)
plt.ylabel('Factor', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x')
st.pyplot(plt.gcf())
