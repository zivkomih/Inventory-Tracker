import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('Primarily Invented for Creative Tax Evasion Tactics (P.I.C.T.E.T) Portfolio Optimizer')

# Willkommens-Nachricht
st.markdown("""
**Willkommen auf Ihrer Investment-Plattform!**

Wir freuen uns, Sie an Bord zu haben, um gemeinsam in Ihre finanzielle Zukunft zu investieren.
Hier können Sie Ihr Portfolio nach Ihrem individuellen Risiko-Rendite-Profil optimieren.
""")

# Risikoprofil-Bewertung
def calculate_risk_profile():
    st.subheader("Risiko-Reward Profilbewertung")
    time_options = {"Weniger als 3 Jahre": 1, "3 bis 10 Jahre": 2, "Mehr als 10 Jahre": 3}
    income_options = {"Weniger als 100.000 CHF": 1, "Zwischen 100.000 und 250.000 CHF": 2, "Mehr als 250.000 CHF": 3}

    time = st.selectbox("Wie lange planen Sie zu investieren?", list(time_options.keys()))
    income = st.selectbox("Wie viel möchten Sie investieren?", list(income_options.keys()))

    time_value = time_options[time]
    income_value = income_options[income]

    finpriority = st.slider("Finanzielle Sicherheit ist mir sehr wichtig.", 1, 4, 3)
    risk = st.slider("Ich bin risikoavers, wenn es um Investitionen geht.", 1, 4, 2)
    high_risk = st.slider("Ich bin bereit, für höhere Renditen höhere Risiken einzugehen.", 1, 4, 2)
    loss = st.slider("Das Risiko von Verlusten beunruhigt mich sehr.", 1, 4, 3)
    min_loss = st.slider("Auch minimale Verluste beunruhigen mich.", 1, 4, 3)

    # Risikoberechnung
    risk_capacity = (time_value + income_value) / 2
    risk_tolerance = (finpriority + risk + high_risk + loss + min_loss) / 5

    if risk_capacity < 2:
        capacity_category = 'Konservativ'
    elif risk_capacity < 3:
        capacity_category = 'Moderat'
    else:
        capacity_category = 'Aggressiv'

    if risk_tolerance < 2:
        tolerance_category = 'Konservativ'
    elif risk_tolerance < 3:
        tolerance_category = 'Moderat'
    else:
        tolerance_category = 'Aggressiv'

    return capacity_category, tolerance_category

# Aufrufen der Funktion und Speichern der Ergebnisse
capacity, tolerance = calculate_risk_profile()
st.write("Ihr Kapazitätsprofil:", capacity)
st.write("Ihr Toleranzprofil:", tolerance)

# Aktienauswahl und -analyse
stock_symbol = st.text_input('Geben Sie das Aktiensymbol ein (z.B. AAPL für Apple):')

if stock_symbol:
    # Abrufen des aktuellen Kurses
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey=DEINSCHLÜSSEL'
    response = requests.get(url)
    data = response.json()
    current_price = data.get('Global Quote', {}).get('05. price', 'Nicht verfügbar')
    st.write(f"Aktueller Kurs von {stock_symbol}: ${current_price}")

    # Historische Daten laden
    end_date = pd.Timestamp.today()
    start_date = end_date - pd.DateOffset(months=3)
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    stock_data['SMA'] = stock_data['Close'].rolling(window=20).mean()
    average_close = stock_data['Close'].mean()
    latest_sma = stock_data['SMA'].iloc[-1]

    # Empfehlung basierend auf Risikoprofil
    recommendation = 'Kaufen' if latest_sma > average_close else 'Verkaufen'
    st.write(f"Empfehlung basierend auf Ihrem Risikoprofil ({tolerance}): {recommendation}")
    st.write(f"Durchschnittlicher Schlusskurs der letzten 3 Monate: ${average_close:.2f}")
    st.write(f"Aktueller gleitender Durchschnitt (SMA): ${latest_sma:.2f}")

    # Darstellung der Aktiendaten
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data['Close'], label='Schlusskurs')
    plt.plot(stock_data['SMA'], label='SMA (20 Tage)')
    plt.title(f'Kursentwicklung von {stock_symbol}')
    plt.legend()
    st.pyplot()
