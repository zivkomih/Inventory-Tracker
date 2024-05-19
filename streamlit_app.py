import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Beispiel-Daten für die Neigung zu verschiedenen Arten von Spiritualität basierend auf den ersten 20 Seiten der Umfrage
data_spirituality_types = {
    'Category': ['Personal Growth', 'Inner Peace', 'Connection with Nature', 'Compassion', 'Purpose in Life'],
    'Percentage': [70, 60, 50, 65, 75]
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

# Erstellen des Spinnennetz-Diagramms
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

ax.fill(angles, values, color='purple', alpha=0.25)
ax.plot(angles, values, color='purple', linewidth=2)

# Kategorien-Labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

# Titel hinzufügen
plt.title('Spirituality Types', size=20, color='purple', y=1.1)

# Anzeige des Diagramms in Streamlit
st.title("Survey Results: Spirituality Types")
st.pyplot(fig)



