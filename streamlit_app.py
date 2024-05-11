import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('Primarily Invented for Creative Tax Evasion Tactics (PICTET)')

# Eingabe des Aktiensymbols durch den Nutzer
stock_symbol = st.text_input('Geben Sie das Aktiensymbol ein (z.B. AAPL für Apple):')

if stock_symbol:
    # Abrufen des aktuellen Kurses über die Alpha Vantage API
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey=NXHHVY2K0P079FB2'
    response = requests.get(url)
    data = response.json()

    try:
        current_price = data['Global Quote']['05. price']
        st.write(f"Aktueller Kurs von {stock_symbol}: ${current_price}")
    except KeyError:
        st.error('Fehler beim Abrufen des aktuellen Kurses. Bitte überprüfen Sie das Symbol und versuchen Sie es erneut.')

    # Laden der historischen Aktiendaten der letzten 3 Monate
    end_date = pd.Timestamp.today()
    start_date = end_date - pd.DateOffset(months=3)
    try:
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        if not stock_data.empty:
            # Berechnung des gleitenden Durchschnitts
            stock_data['SMA'] = stock_data['Close'].rolling(window=3).mean()

            # Durchschnittlicher Schlusskurs der letzten 3 Monate
            average_close = stock_data['Close'].mean()
            # Aktueller gleitender Durchschnitt (SMA)
            latest_sma = stock_data['SMA'].iloc[-1]

            # Entscheidungsempfehlung basierend auf Preisvergleich
            recommendation = 'Kaufen' if stock_data['Close'].iloc[-1] > latest_sma else 'Verkaufen'

            # Darstellung der Aktiendaten und der Empfehlungen am Ende der Seite
            st.subheader('Kursentwicklung der letzten 3 Monate')
            plt.figure(figsize=(10, 6))
            plt.plot(stock_data['Close'], label='Schlusskurs')
            plt.plot(stock_data['SMA'], label='SMA')
            plt.title(f'Kursentwicklung für {stock_symbol}')
            plt.xlabel('Datum')
            plt.ylabel('Schlusskurs ($)')
            plt.legend()
            st.pyplot()

            st.write(f"Empfehlung: {recommendation}")
            st.write(f"Durchschnittlicher Schlusskurs der letzten 3 Monate: ${average_close:.2f}")
            st.write(f"Aktueller gleitender Durchschnitt (SMA): ${latest_sma:.2f}")
        else:
            st.error('Keine historischen Daten für das Symbol gefunden.')

    except Exception as e:
        st.error(f'Fehler beim Laden der Daten: {e}')

    # Option, dieser Aktie zu folgen
    follow_stock = st.checkbox('Dieser Aktie folgen')
    if follow_stock:
        st.write('Sie folgen jetzt der Aktie', stock_symbol)
