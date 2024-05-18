import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Datei-Upload-Widget
uploaded_file = st.file_uploader("Wähle eine Excel-Datei aus", type=["xls", "xlsx"])

if uploaded_file is not None:
    try:
        # Datei einlesen
        df = pd.read_excel(uploaded_file)

        # Fehlende Daten bereinigen (Beispiel: Ersetze -77 und -99 durch NaN)
        df = df.replace([-77, -99], np.nan)

        # Zeige die ersten Zeilen und Datentypen vor der Transposition
        st.write("Erste Zeilen des ursprünglichen DataFrames")
        st.write(df.head())
        st.write("Datentypen der Spalten vor der Transposition")
        st.write(df.dtypes)

        # Versuche, die Daten in numerische Typen zu konvertieren, falls möglich
        df = df.apply(pd.to_numeric, errors='coerce')

        # Transponiere den DataFrame
        df = df.T

        # Zeige die ersten Zeilen und Datentypen nach der Transposition
        st.write("Erste Zeilen des transponierten DataFrames")
        st.write(df.head())
        st.write("Datentypen der Spalten nach der Transposition")
        st.write(df.dtypes)

        # Deskriptive Statistiken
        st.write("Deskriptive Statistiken")
        st.write(df.describe())

        # Nur numerische Spalten auswählen
        numerical_df = df.select_dtypes(include=[np.number])

        # Überprüfen der numerischen Daten
        st.write("Numerische Daten")
        st.write(numerical_df.head())
        st.write(numerical_df.describe())

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
    except Exception as e:
        st.error(f"Fehler beim Verarbeiten der Datei: {e}")
else:
    st.write("Bitte lade eine Excel-Datei hoch.")
