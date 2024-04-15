import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('Primarily Invented for Creative Tax Evasion Tactics (PICTET)')

# Auswahl der Aktie
stock_symbol = st.text_input('Geben Sie das Aktiensymbol ein (z.B. AAPL für Apple):')

if stock_symbol:
    # API URL für den aktuellen Kurs
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey=NXHHVY2K0P079FB2'
    response = requests.get(url)
    data = response.json()

    try:
        current_price = data['Global Quote']['05. price']
        st.write(f"Aktueller Kurs von {stock_symbol}: ${current_price}")
    except KeyError:
        st.error('Fehler beim Abrufen des aktuellen Kurses. Bitte überprüfen Sie das Symbol und versuchen Sie es erneut.')

    # Laden der Aktiendaten
    try:
        stock_data = yf.download(stock_symbol, start='2022-01-01', end='2022-12-31')
        if not stock_data.empty:
            st.write(stock_data.head())  # Anzeige der ersten paar Zeilen der Aktiendaten

            # Berechnung des gleitenden Durchschnitts
            stock_data['SMA'] = stock_data['Close'].rolling(window=3).mean()
            latest_close = stock_data['Close'].iloc[-1]
            latest_sma = stock_data['SMA'].iloc[-1]

            if latest_close > latest_sma:
                recommendation = 'Kaufen'
            else:
                recommendation = 'Verkaufen'
            
            st.write(f"Empfehlung: {recommendation}")

            # Darstellung der Aktiengrafik
            st.subheader('Historische Kursdaten')
            plt.figure(figsize=(10, 6))
            plt.plot(stock_data['Close'], label='Schlusskurs')
            plt.plot(stock_data['SMA'], label='SMA')
            plt.title('Historische Kursdaten für ' + stock_symbol)
            plt.xlabel('Datum')
            plt.ylabel('Schlusskurs ($)')
            plt.legend()
            st.pyplot()
        else:
            st.error('Keine historischen Daten für das Symbol gefunden.')

    except Exception as e:
        st.error(f'Fehler beim Laden der Daten: {e}')

    # Folgeoption
    follow_stock = st.checkbox('Dieser Aktie folgen')
    if follow_stock:
        st.write('Sie folgen jetzt der Aktie', stock_symbol)
