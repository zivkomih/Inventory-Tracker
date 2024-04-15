import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests

# API-Key Finanzdaten
api_key = 'NXHHVY2K0P079FB2'
symbol = st.text_input("Gib den Aktiennamen ein (z.B. AAPL für Apple):")

if symbol:
    # API URL für den aktuellen Kurs
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    current_price = data['Global Quote']['05. price']
    st.write(f"Aktueller Kurs von {symbol}: ${current_price}")

    # Beispiel-Datenframe
df = pd.DataFrame({
    'date': ['2023-04-10', '2023-04-11', '2023-04-12', '2023-04-13', '2023-04-14'],
    'close': [150, 152, 153, 155, 154]
})

# Berechnung des gleitenden Durchschnitts
df['SMA'] = df['close'].rolling(window=3).mean()

# Aktuellen Kurs und SMA vergleichen
latest_close = df.iloc[-1]['close']
latest_sma = df.iloc[-1]['SMA']

if latest_close > latest_sma:
    recommendation = 'Kaufen'
else:
    recommendation = 'Verkaufen'

st.write(f"Empfehlung: {recommendation}")

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
