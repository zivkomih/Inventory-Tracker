import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Datei einlesen
file_path = r"C:\Users\mihae\Downloads\Porsche Survey Results.xls"
df = pd.read_excel(file_path)

# Fehlende Daten bereinigen (Beispiel: Ersetze -77 und -99 durch NaN)
df = df.replace([-77, -99], pd.NA)

# Deskriptive Statistiken
st.write("Deskriptive Statistiken")
st.write(df.describe())

# Korrelationen berechnen
correlation_matrix = df.corr()
st.write("Korrelationen")
st.write(correlation_matrix)

# Heatmap der Korrelationen
st.write("Heatmap der Korrelationen")
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
st.pyplot(plt)
