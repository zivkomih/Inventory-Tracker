import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title('Trading App')

# Auswahl der Aktie
stock_symbol = st.text_input('Geben Sie das Aktiensymbol ein (z.B. AAPL für Apple):')

# Laden der Aktiendaten
if stock_symbol:
    try:
        stock_data = yf.download(stock_symbol, start='2022-01-01', end='2022-12-31')
        st.write(stock_data.head())  # Anzeige der ersten paar Zeilen der Aktiendaten

        # Darstellung der Aktiengrafik
        st.subheader('Historische Kursdaten')
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data['Close'])
        plt.title('Historische Kursdaten für ' + stock_symbol)
        plt.xlabel('Datum')
        plt.ylabel('Schlusskurs ($)')
        st.pyplot()

        # Folgeoption
        follow_stock = st.checkbox('Dieser Aktie folgen')

        if follow_stock:
            st.write('Sie folgen jetzt der Aktie', stock_symbol)
            # Hier könnten Sie Logik hinzufügen, um Empfehlungen basierend auf den Kursdaten zu generieren.

    except Exception as e:
        st.write('Fehler beim Laden der Daten:', e)
