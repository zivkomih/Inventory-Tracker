import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Beispiel-Daten erstellen basierend auf den Informationen
data_values_beliefs = {
    'Category': ['Spiritualität', 'Lebensbalance', 'Ökologische Nachhaltigkeit', 'Finanzieller Wohlstand', 'Beziehungen'],
    'Percentage': [20, 81, 8, 43, 86]
}

data_luxury_purchase = {
    'Category': ['Interesse an Luxusgütern', 'Kaufmotive: Qualität', 'Kaufmotive: Komfort', 'Markenpräferenzen: Porsche', 'Markenpräferenzen: Ferrari', 'Markenpräferenzen: Lamborghini'],
    'Percentage': [28, 66, 62, 53, 53, 53]
}

data_mobility_preferences = {
    'Category': ['Nutzung öffentlicher Verkehrsmittel', 'Autonutzung', 'Flugreisen', 'Fahrradnutzung', 'Car-Sharing', 'Transportkriterien: Bequemlichkeit', 'Transportkriterien: Praktikabilität'],
    'Percentage': [38, 45, 23, 15, 5, 62, 68]
}

data_porsche_spirituality = {
    'Category': ['Porsche und Spiritualität: Ja', 'Porsche und Spiritualität: Nein'],
    'Percentage': [19, 81]
}

# Create DataFrames
df_values_beliefs = pd.DataFrame(data_values_beliefs)
df_luxury_purchase = pd.DataFrame(data_luxury_purchase)
df_mobility_preferences = pd.DataFrame(data_mobility_preferences)
df_porsche_spirituality = pd.DataFrame(data_porsche_spirituality)

# Set style for the plots
sns.set(style="whitegrid")

st.title("Umfrageergebnisse")

# Plot 1: Werte und Überzeugungen
st.subheader('Werte und Überzeugungen')
plt.figure(figsize=(10, 6))
sns.barplot(x='Percentage', y='Category', data=df_values_beliefs, palette="viridis")
plt.title('Werte und Überzeugungen')
plt.xlabel('Prozent')
plt.ylabel('')
st.pyplot(plt.gcf())

# Plot 2: Luxuskaufentscheidungen
st.subheader('Luxuskaufentscheidungen')
plt.figure(figsize=(10, 6))
sns.barplot(x='Percentage', y='Category', data=df_luxury_purchase, palette="plasma")
plt.title('Luxuskaufentscheidungen')
plt.xlabel('Prozent')
plt.ylabel('')
st.pyplot(plt.gcf())

# Plot 3: Mobilitätspräferenzen
st.subheader('Mobilitätspräferenzen')
plt.figure(figsize=(10, 6))
sns.barplot(x='Percentage', y='Category', data=df_mobility_preferences, palette="cubehelix")
plt.title('Mobilitätspräferenzen')
plt.xlabel('Prozent')
plt.ylabel('')
st.pyplot(plt.gcf())

# Plot 4: Verbindung zwischen Porsche und Spiritualität
st.subheader('Verbindung zwischen Porsche und Spiritualität')
plt.figure(figsize=(10, 6))
sns.barplot(x='Percentage', y='Category', data=df_porsche_spirituality, palette="magma")
plt.title('Verbindung zwischen Porsche und Spiritualität')
plt.xlabel('Prozent')
plt.ylabel('')
st.pyplot(plt.gcf())
