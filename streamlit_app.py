import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Beispiel-Daten basierend auf den vorherigen Informationen
data = {
    'Spirituality Importance': [4, 5, 6, 5, 6, 4, 5, 6, 5, 6],
    'Life Balance Importance': [5, 6, 7, 6, 7, 5, 6, 7, 6, 7],
    'Environmental Sustainability Importance': [3, 2, 1, 2, 1, 3, 2, 1, 2, 1],
    'Financial Prosperity Importance': [6, 5, 4, 5, 6, 6, 5, 4, 5, 6],
    'Relationships Importance': [7, 6, 5, 6, 7, 7, 6, 5, 6, 7],
    'Interest in Luxury Goods': [2, 3, 4, 3, 4, 2, 3, 4, 3, 4],
    'Purchase Motive Quality': [6, 6, 7, 6, 7, 6, 6, 7, 6, 7],
    'Purchase Motive Comfort': [5, 5, 6, 5, 6, 5, 5, 6, 5, 6],
    'Brand Preference Porsche': [4, 5, 6, 5, 6, 4, 5, 6, 5, 6],
    'Brand Preference Ferrari': [3, 4, 5, 4, 5, 3, 4, 5, 4, 5],
    'Brand Preference Lamborghini': [2, 3, 4, 3, 4, 2, 3, 4, 3, 4],
    'Use of Public Transport': [5, 4, 3, 4, 3, 5, 4, 3, 4, 3],
    'Car Usage': [6, 7, 6, 7, 6, 6, 7, 6, 7, 6],
    'Air Travel': [4, 3, 2, 3, 2, 4, 3, 2, 3, 2],
    'Bicycle Usage': [3, 2, 1, 2, 1, 3, 2, 1, 2, 1],
    'Car Sharing': [2, 1, 0, 1, 0, 2, 1, 0, 1, 0],
    'Transport Criteria Convenience': [6, 7, 6, 7, 6, 6, 7, 6, 7, 6],
    'Transport Criteria Practicality': [5, 6, 5, 6, 5, 5, 6, 5, 6, 5]
}

df = pd.DataFrame(data)

# Korrelationen berechnen
correlation_matrix = df.corr()

# Set style for the plots
sns.set(style="whitegrid")

st.title("Survey Results and Correlations")

# Plot: Simplified Correlation Heatmap
st.subheader('Simplified Correlation Heatmap')
plt.figure(figsize=(10, 8))
mask = correlation_matrix.abs() < 0.5  # Mask less significant correlations
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, mask=mask, cbar_kws={'label': 'Correlation Coefficient'})
plt.title('Simplified Correlation Matrix', fontsize=16)
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)
st.pyplot(plt.gcf())



