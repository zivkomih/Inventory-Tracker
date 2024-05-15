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

    # Laden der Aktiendaten für die letzten 3 Monate
    end_date = pd.Timestamp.today()  # heutiges Datum
    start_date = end_date - pd.DateOffset(months=3)  # Datum vor drei Monaten
    try:
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        if not stock_data.empty:
            st.write(stock_data.head())  # Anzeige der ersten paar Zeilen der Aktiendaten

            # Berechnung des gleitenden Durchschnitts
            stock_data['SMA'] = stock_data['Close'].rolling(window=3).mean()
            latest_close = stock_data['Close'].iloc[-1]
            latest_sma = stock_data['SMA'].iloc[-1]

            # Durchschnitt der Schlusskurse über die letzten 3 Monate
            average_close = stock_data['Close'].mean()

            if latest_close > latest_sma:
                recommendation = 'Kaufen'
            else:
                recommendation = 'Verkaufen'

            st.write(f"Empfehlung: {recommendation}")
            st.write(f"Durchschnittlicher Schlusskurs der letzten 3 Monate: ${average_close:.2f}")
            st.write(f"Aktueller gleitender Durchschnitt (SMA): ${latest_sma:.2f}")

            # Darstellung der Aktiengrafik
            st.subheader('Kursentwicklung der letzten 3 Monate')
            plt.figure(figsize=(10, 6))
            plt.plot(stock_data['Close'], label='Schlusskurs')
            plt.plot(stock_data['SMA'], label='SMA')
            plt.title('Kursentwicklung für ' + stock_symbol)
            plt.xlabel('Datum')
            plt.ylabel('Schlusskurs ($)')
            plt.legend()
            st.pyplot()

            # Portfolioverteilung hinzufügen (Beispiel)
            st.subheader('Portfolio Distribution')
            portfolio = {
                "AAPL": 20,
                "GOOGL": 30,
                "MSFT": 25,
                "AMZN": 25
            }
            fig, ax = plt.subplots()
            ax.pie(portfolio.values(), labels=portfolio.keys(), autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Gleiches Seitenverhältnis stellt sicher, dass die Pie als Kreis gezeichnet wird.
            st.pyplot(fig)
        else:
            st.error('Keine historischen Daten für das Symbol gefunden.')

    except Exception as e:
        st.error(f'Fehler beim Laden der Daten: {e}')

    # Folgeoption
    follow_stock = st.checkbox('Dieser Aktie folgen')
    if follow_stock:
        st.write('Sie folgen jetzt der Aktie', stock_symbol)
