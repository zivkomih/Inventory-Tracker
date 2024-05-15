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

# Definition der Risikoklassifikationen auf Deutsch
def determine_risk_appetite_category(risk_appetite):
    if risk_appetite < 2.5:
        return "Verringert"
    elif risk_appetite < 3.5:
        return "Mittel"
    else:
        return "Erhöht"

def determine_risk_capacity_category(risk_capacity):
    if risk_capacity <= 1.5:
        return "Tief"
    elif risk_capacity <= 2.5:
        return "Mittel"
    else:
        return "Hoch"

def determine_risk_profile_category(risk_profile):
    if risk_profile < 2:
        return "Konservativ"
    elif risk_profile < 3:
        return "Moderat Konservativ"
    elif risk_profile < 4:
        return "Moderat"
    elif risk_profile < 5:
        return "Moderat Aggressiv"
    else:
        return "Aggressiv"

# Risikoprofil-Bewertung
def calculate_risk_profile():
    st.subheader("Risiko-Reward Profilbewertung")
    time_options = {"Weniger als 3 Jahre": 1, "3 bis 10 Jahre": 2, "Mehr als 10 Jahre": 3}
    income_options = {"Weniger als 100.000 CHF": 1, "Zwischen 100.000 und 250.000 CHF": 2, "Mehr als 250.000 CHF": 3}

    time = st.selectbox("Wie lange planen Sie zu investieren?", list(time_options.keys()))
    income = st.selectbox("Wie viel möchten Sie investieren?", list(income_options.keys()))

    time_value = time_options[time]
    income_value = income_options[income]

    options = ["Vollständig dagegen", "Eher dagegen", "Eher dafür", "Vollständig dafür"]
    finpriority = st.select_slider("Finanzielle Sicherheit ist mir sehr wichtig.", options=options, value="Vollständig dafür")
    risk = st.select_slider("Ich bin risikoavers, wenn es um Investitionen geht.", options=options, value="Eher dafür")
    high_risk = st.select_slider("Ich bin bereit, für höhere Renditen höhere Risiken einzugehen.", options=options, value="Eher dafür")
    loss = st.select_slider("Das Risiko von Verlusten beunruhigt mich sehr.", options=options, value="Eher dafür")
    min_loss = st.select_slider("Auch minimale Verluste beunruhigen mich.", options=options, value="Eher dafür")

    slider_values = {"Vollständig dagegen": 1, "Eher dagegen": 2, "Eher dafür": 3, "Vollständig dafür": 4}
    risk_appetite = (slider_values[finpriority] + slider_values[high_risk]) / 2
    risk_capacity = (time_value + income_value) / 2
    risk_profile = (slider_values[risk] + slider_values[loss] + slider_values[min_loss]) / 3

    appetite_category = determine_risk_appetite_category(risk_appetite)
    capacity_category = determine_risk_capacity_category(risk_capacity)
    profile_category = determine_risk_profile_category(risk_profile)

    return appetite_category, capacity_category, profile_category

appetite_category, capacity_category, profile_category = calculate_risk_profile()
st.write("Ihr Risiko Appetit:", appetite_category)
st.write("Ihr Kapazitätsprofil:", capacity_category)
st.write("Ihr Risikoprofil:", profile_category)

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
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    if not stock_data.empty:
        stock_data['SMA'] = stock_data['Close'].rolling(window=3).mean()  # Berechnung des gleitenden Durchschnitts
        latest_close = stock_data['Close'].iloc[-1]
        latest_sma = stock_data['SMA'].iloc[-1]

        # Durchschnitt der Schlusskurse über die letzten 3 Monate
        average_close = stock_data['Close'].mean()

        # Empfehlung mit Hervorhebung darstellen
        if latest_close > latest_sma:
            recommendation = 'Kaufen'
            st.success(f"Empfehlung: {recommendation}")
        else:
            recommendation = 'Verkaufen'
            st.error(f"Empfehlung: {recommendation}")

        st.write(f"Durchschnittlicher Schlusskurs der letzten 3 Monate: ${average_close:.2f}")
        st.write(f"Aktueller gleitender Durchschnitt (SMA): ${latest_sma:.2f}")

        # Erste Grafik: Kursentwicklung
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(stock_data['Close'], label='Schlusskurs')
        ax.plot(stock_data['SMA'], label='SMA')
        ax.set_title('Kursentwicklung für ' + stock_symbol)
        ax.set_xlabel('Datum')
        ax.set_ylabel('Schlusskurs ($)')
        ax.legend()
        st.pyplot(fig)

        # Zweite Grafik: Beispiel für eine Portfolioverteilung
        st.subheader('Beispielhafte Portfolioverteilung')
        portfolio_data = {"AAPL": 30, "MSFT": 30, "GOOGL": 20, "AMZN": 20}
        fig2, ax2 = plt.subplots()
        ax2.pie(portfolio_data.values(), labels=portfolio_data.keys(), autopct='%1.1f%%', startangle=90)
        ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig2)

    else:
        st.error('Keine historischen Daten für das Symbol gefunden.')

