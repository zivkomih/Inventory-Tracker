import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Beispiel-Daten basierend auf den vorherigen Informationen
data = {
    'Age': [21, 22, 23, 24, 25],
    'Spirituality_Importance': [4, 5, 6, 5, 6],
    'Life_Balance_Importance': [5, 6, 7, 6, 7],
    'Environmental_Sustainability_Importance': [3, 2, 1, 2, 1],
    'Financial_Prosperity_Importance': [6, 5, 4, 5, 6],
    'Relationships_Importance': [7, 6, 5, 6, 7],
    'Interest_in_Luxury_Goods': [2, 3, 4, 3, 4],
    'Purchase_Motive_Quality': [6, 6, 7, 6, 7],
    'Purchase_Motive_Comfort': [5, 5, 6, 5, 6],
    'Brand_Preference_Porsche': [4, 5, 6, 5, 6],
    'Brand_Preference_Ferrari': [3, 4, 5, 4, 5],
    'Brand_Preference_Lamborghini': [2, 3, 4, 3, 4],
    'Use_of_Public_Transport': [5, 4, 3, 4, 3],
    'Car_Usage': [6, 7, 6, 7, 6],
    'Air_Travel': [4, 3, 2, 3, 2],
    'Bicycle_Usage': [3, 2, 1, 2, 1],
    'Car_Sharing': [2, 1, 0, 1, 0],
    'Transport_Criteria_Convenience': [6, 7, 6, 7, 6],
    'Transport_Criteria_Practicality': [5, 6, 5, 6, 5],
    'Porsche_and_Spirituality_Yes': [1, 0, 1, 0, 1],
    'Porsche_and_Spirituality_No': [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Korrelationen berechnen
correlation_matrix = df.corr()

# Set style for the plots
sns.set(style="whitegrid")

st.title("Survey Results and Correlations")

# Plot: Correlation Heatmap
st.subheader('Correlation Heatmap')
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix', fontsize=16)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
st.pyplot(plt.gcf())

