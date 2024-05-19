import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Beispiel-Daten für die Neigung zu verschiedenen Arten von Spiritualität
data_spirituality_types = {
    'Category': ['Religious', 'Spiritual but not Religious', 'Mystical', 'Humanistic', 'Nature-Oriented', 'Existential'],
    'Percentage': [30, 40, 20, 35, 25, 15]
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

# Stil für die Diagramme festlegen
sns.set(style="whitegrid")

st.title("Survey Results")

# Farben definieren
colors = ["#EBD698", "#000000", "#B12B28"]

# Plot 1: Values and Beliefs
data_values_beliefs = {
    'Category': ['Spirituality', 'Life Balance', 'Environmental Sustainability', 'Financial Prosperity', 'Relationships', 'Personal Development'],
    'Percentage': [20, 81, 8, 43, 86, 75]
}
df_values_beliefs = pd.DataFrame(data_values_beliefs).sort_values(by='Percentage', ascending=False)

st.subheader('Values and Beliefs')
plt.figure(figsize=(12, 7))
sns.barplot(x='Percentage', y='Category', data=df_values_beliefs, palette=colors)
plt.title('Values and Beliefs', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x')
st.pyplot(plt.gcf())

# Plot 2: Luxury Purchase Decisions
data_luxury_purchase_expanded = {
    'Category': [
        'Interest in Luxury Goods',
        'Purchase Motive: Quality',
        'Purchase Motive: Comfort',
        'Purchase Motive: Technology',
        'Purchase Motive: Status Symbol',
        'Purchase Motive: Brand Image',
        'Purchase Motive: Design',
        'Purchase Motive: Exclusivity',
        'Purchase Motive: Investment Value',
        'Purchase Motive: Customer Service',
        'Purchase Motive: Sustainability',
        'Purchase Motive: Performance',
        'Purchase Motive: Safety',
        'Purchase Motive: Heritage'
    ],
    'Percentage': [
        28, 66, 62, 50, 45, 60, 55, 40, 35, 30, 25, 70, 65, 55
    ]
}
df_luxury_purchase_expanded = pd.DataFrame(data_luxury_purchase_expanded).sort_values(by='Percentage', ascending=False)

st.subheader('Luxury Purchase Decisions')
plt.figure(figsize=(12, 7))
sns.barplot(x='Percentage', y='Category', data=df_luxury_purchase_expanded, palette=colors)
plt.title('Luxury Purchase Decisions', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x')
st.pyplot(plt.gcf())

# Plot 3: Mobility Preferences and Transport Criteria
data_mobility_preferences = {
    'Category': ['Use of Public Transport', 'Car Usage', 'Air Travel', 'Bicycle Usage', 'Car Sharing'],
    'Percentage': [38, 45, 23, 15, 5]
}
data_transport_criteria = {
    'Category': ['Transport Criteria: Convenience', 'Transport Criteria: Practicality'],
    'Percentage': [62, 68]
}
df_mobility_preferences = pd.DataFrame(data_mobility_preferences).sort_values(by='Percentage', ascending=False)
df_transport_criteria = pd.DataFrame(data_transport_criteria).sort_values(by='Percentage', ascending=False)

st.subheader('Mobility Preferences and Transport Criteria')
plt.figure(figsize=(12, 7))
df_combined = pd.concat([df_mobility_preferences, df_transport_criteria])
df_combined['Type'] = ['Mobility Preferences'] * len(df_mobility_preferences) + ['Transport Criteria'] * len(df_transport_criteria)

sns.barplot(x='Percentage', y='Category', hue='Type', data=df_combined, palette=colors[:2])
plt.title('Mobility Preferences and Transport Criteria', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Type', loc='upper right')
plt.grid(axis='x')
st.pyplot(plt.gcf())

# Plot 4: Connection between Porsche and Spirituality
data_porsche_spirituality = {
    'Category': ['Porsche and Spirituality: Yes', 'Porsche and Spirituality: No'],
    'Percentage': [19, 81]
}
df_porsche_spirituality = pd.DataFrame(data_porsche_spirituality).sort_values(by='Percentage', ascending=False)

st.subheader('Connection between Porsche and Spirituality')
plt.figure(figsize=(12, 7))
sns.barplot(x='Percentage', y='Category', data=df_porsche_spirituality, palette=colors)
plt.title('Connection between Porsche and Spirituality', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x')
st.pyplot(plt.gcf())

# Plot 5: Spirituality Types (Spider Chart)
st.subheader('Spirituality Types')
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

ax.fill(angles, values, color=colors[2], alpha=0.25)
ax.plot(angles, values, color=colors[2], linewidth=2)

# Kategorien-Labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

# Titel hinzufügen
plt.title('Spirituality Types', size=20, color=colors[2], y=1.1)
st.pyplot(fig)

