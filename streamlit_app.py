import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Beispiel-Daten basierend auf den Informationen aus dem PDF-Dokument
data = {
    'Spirituality_Importance': [4, 5, 6, 5, 6, 3, 6, 5, 2, 2, 5, 2, 2, 1, 7, 4, 6, 6, 5, 1, 4, 1, 1, 5, 1, 6, 2, 7, 5, 5, 1, 5, 6, 3, 5, 1, 4, 6, 2, 4, 4, 5, 2, 1, 2, 6, 6, 3, 6, 3, 4, 2],
    'Life_Balance_Importance': [7, 6, 7, 5, 7, 4, 7, 5, 4, 3, 5, 3, 4, 2, 7, 6, 7, 7, 5, 2, 6, 3, 3, 7, 3, 7, 4, 7, 6, 6, 3, 6, 7, 4, 6, 3, 5, 7, 3, 6, 5, 7, 4, 3, 4, 7, 7, 4, 6, 4, 5, 3],
    'Environmental_Sustainability_Importance': [3, 4, 5, 2, 4, 1, 4, 3, 2, 2, 3, 1, 2, 1, 6, 4, 4, 4, 3, 1, 4, 2, 2, 4, 2, 5, 3, 5, 4, 4, 2, 3, 5, 3, 4, 2, 4, 5, 2, 4, 3, 4, 3, 2, 3, 5, 5, 2, 4, 3, 3, 2],
    'Financial_Prosperity_Importance': [6, 6, 6, 5, 7, 4, 7, 6, 3, 3, 6, 3, 4, 2, 7, 5, 7, 6, 5, 2, 6, 3, 3, 6, 3, 6, 4, 6, 6, 5, 3, 5, 6, 4, 6, 3, 5, 7, 4, 5, 4, 6, 3, 3, 3, 7, 6, 3, 6, 3, 4, 3],
    'Relationships_Importance': [7, 7, 6, 6, 7, 5, 7, 6, 4, 3, 6, 3, 4, 2, 7, 7, 7, 7, 6, 2, 7, 3, 3, 7, 3, 7, 4, 7, 6, 6, 3, 6, 7, 4, 6, 3, 5, 7, 4, 6, 5, 7, 4, 3, 4, 7, 7, 4, 6, 4, 5, 3],
    'Interest_in_Luxury_Goods': [2, 3, 3, 2, 3, 1, 3, 2, 1, 1, 2, 1, 1, 1, 4, 3, 3, 3, 2, 1, 3, 1, 1, 3, 1, 3, 2, 4, 3, 3, 1, 3, 3, 2, 3, 1, 2, 3, 1, 3, 2, 3, 2, 1, 2, 4, 3, 1, 3, 2, 2, 1],
    'Purchase_Motive_Quality': [6, 6, 7, 6, 7, 5, 7, 6, 4, 4, 6, 4, 5, 3, 7, 6, 7, 7, 6, 3, 6, 4, 4, 7, 4, 7, 5, 7, 6, 6, 4, 6, 7, 5, 6, 4, 5, 7, 5, 6, 5, 7, 5, 4, 5, 7, 7, 4, 6, 4, 5, 4],
    'Purchase_Motive_Comfort': [5, 5, 6, 5, 6, 4, 6, 5, 3, 3, 5, 3, 4, 2, 7, 6, 6, 6, 5, 2, 6, 3, 3, 6, 3, 6, 4, 6, 5, 5, 3, 5, 6, 4, 5, 3, 5, 6, 3, 5, 4, 6, 4, 3, 4, 6, 6, 4, 5, 4, 5, 3],
    'Brand_Preference_Porsche': [4, 5, 6, 5, 6, 4, 6, 5, 3, 3, 5, 3, 4, 2, 7, 6, 6, 6, 5, 2, 6, 3, 3, 6, 3, 6, 4, 6, 5, 5, 3, 5, 6, 4, 5, 3, 5, 6, 3, 5, 4, 6, 4, 3, 4, 6, 6, 4, 5, 4, 5, 3],
    'Brand_Preference_Ferrari': [3, 4, 5, 4, 5, 3, 5, 4, 2, 2, 4, 2, 3, 2, 6, 5, 5, 5, 4, 2, 5, 2, 2, 5, 2, 5, 3, 5, 4, 4, 2, 4, 5, 3, 4, 2, 4, 5, 2, 4, 3, 5, 3, 2, 3, 5, 5, 2, 4, 3, 4, 2],
    'Brand_Preference_Lamborghini': [2, 3, 4, 3, 4, 2, 4, 3, 1, 1, 3, 1, 2, 1, 5, 4, 4, 4, 3, 1, 4, 1, 1, 4, 1, 4, 2, 4, 3, 3, 1, 3, 4, 2, 3, 1, 3, 4, 1, 3, 2, 4, 2, 1, 2, 4, 4, 1, 3, 2, 3, 1]
}

df = pd.DataFrame(data)

# Korrelationen berechnen
correlation_matrix = df.corr()

# Set style for the plots
sns.set(style="whitegrid")

st.title("Survey Results and Correlations")

# Plot: Simplified Correlation Heat &#8203;``【oaicite:0】``&#8203;
