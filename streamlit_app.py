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
    capacity

