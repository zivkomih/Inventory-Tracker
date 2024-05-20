import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Neue Daten für die Begriffe und Prozentsätze basierend auf der Umfrage
data_values_beliefs = {
    'Category': [
        'Self-perception', 'Balanced life', 'Ecological sustainability', 
        'Financial prosperity', 'Meaningful relationships', 'Personal development'
    ],
    'Percentage': [19, 81, 31, 69, 86, 79]
}

# Erstellen des DataFrames
df_values_beliefs = pd.DataFrame(data_values_beliefs)

# Erstellen der Daten für das Spinnennetz-Diagramm
categories = df_values_beliefs['Category'].tolist()
values = df_values_beliefs['Percentage'].tolist()

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
plt.title('Values and Beliefs', size=20, color='#B12B28', y=1.1)

# Anzeige des Diagramms in Streamlit
st.title("Survey Results: Values and Beliefs")
st.pyplot(fig)
