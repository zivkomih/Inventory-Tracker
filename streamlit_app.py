import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Beispiel-Daten für die Neigung zu verschiedenen Arten von Spiritualität basierend auf der Umfrage
data_spirituality_types = {
    'Category': [
        'Personal Growth', 'Inner Peace', 'Connection with Nature', 'Compassion', 'Purpose in Life',
        'Mindfulness', 'Self-Reflection', 'Gratitude', 'Meditation', 'Religious Practices'
    ],
    'Percentage': [70, 60, 50, 65, 75, 55, 45, 35, 40, 30]
}

# Erstellen des DataFrames
df_spirituality_types = pd.DataFrame(data_spirituality_types)

# Erstellen der Daten für das Spinnennetz-Diagramm
categories = df_spirituality_types['Category'].tolist()
values = df_spirituality_types['Percentage'].tolist()

# Anzahl der Kategorien
num_vars = len(categories)

# Berechnung der Winkel der Kategorien
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Wiederholen der Werte, um das Diagramm zu schließen
values += values[:1]
angles += angles[:1]

# Erstellen des Spinnennetz-Diagramms mit den gewünschten Farben
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.fill(angles, values, color='#EBD698', alpha=0.25)
ax.plot(angles, values, color='#B12B28', linewidth=2)

# Kategorien-Labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='#000000')

# Titel hinzufügen
plt.title('Spirituality Types', size=20, color='#B12B28', y=1.1)

# Anzeige des Diagramms in Streamlit
st.title("Survey Results: Spirituality Types")
st.pyplot(fig)
