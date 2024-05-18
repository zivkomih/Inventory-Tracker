import pandas as pd
import openpyxl
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Datei einlesen
file_path = 'Porsche Survey Results.xlsx'  # Der Pfad zur hochgeladenen Datei
df = pd.read_excel(file_path, engine='openpyxl')

# Fehlende Daten bereinigen (Beispiel: Ersetze -77 und -99 durch NaN)
df = df.replace([-77, -99], np.nan)

# Transponiere den DataFrame
df = df.T

# Zeige die ersten Zeilen des transponierten DataFrames an
st.write("Erste Zeilen des transponierten DataFrames")
st.write(df.head())

# Zeige die Datentypen der Spalten an
st.write("Datentypen der Spalten")
st.write(df.dtypes)

# Deskriptive Statistiken
st.write("Deskriptive Statistiken")
st.write(df.describe())

# Nur numerische Spalten auswählen
numerical_df = df.select_dtypes(include=[np.number])

# Korrelationen berechnen
correlation_matrix = numerical_df.corr()

# Überprüfen der Korrelationen
st.write("Korrelationen")
st.write(correlation_matrix)

# Bereinigung der Korrelationen (Entfernen von NaN-Werten)
cleaned_correlation_matrix = correlation_matrix.dropna(how='all').dropna(axis=1, how='all')

# Heatmap der Korrelationen
if not cleaned_correlation_matrix.empty:
    st.write("Heatmap der Korrelationen")
    plt.figure(figsize=(10, 8))
    sns.heatmap(cleaned_correlation_matrix, annot=True, cmap='coolwarm')
    st.pyplot(plt)
else:
    st.write("Keine gültigen Korrelationen vorhanden.")
