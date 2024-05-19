import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Beispiel-Daten basierend auf den bereitgestellten Informationen
data_values_beliefs = {
    'Category': ['Spirituality', 'Life Balance', 'Environmental Sustainability', 'Financial Prosperity', 'Relationships'],
    'Percentage': [20, 81, 8, 43, 86]
}

data_luxury_purchase_expanded = {
    'Category': [
        'Interest in Luxury Goods',
        'Purchase Motive: Quality',
        'Purchase Motive: Comfort',
        'Purchase Motive: Technology',
        'Purchase Motive: Status Symbol',
        'Purchase Motive: Brand Image',
        'Purchase Motive: Design',
        'Purchase Motive: Exclusivity',
        'Purchase Motive: Investment Value',
        'Purchase Motive: Customer Service',
        'Purchase Motive: Sustainability',
        'Purchase Motive: Performance',
        'Purchase Motive: Safety',
        'Purchase Motive: Heritage'
    ],
    'Percentage': [
        28, 66, 62, 50, 45, 60, 55, 40, 35, 30, 25, 70, 65, 55
    ]
}

data_mobility_preferences = {
    'Category': ['Use of Public Transport', 'Car Usage', 'Air Travel', 'Bicycle Usage', 'Car Sharing'],
    'Percentage': [38, 45, 23, 15, 5]
}

data_transport_criteria = {
    'Category': ['Transport Criteria: Convenience', 'Transport Criteria: Practicality'],
    'Percentage': [62, 68]
}

data_porsche_spirituality = {
    'Category': ['Porsche and Spirituality: Yes', 'Porsche and Spirituality: No'],
    'Percentage': [19, 81]
}

# Erstellen von DataFrames
df_values_beliefs = pd.DataFrame(data_values_beliefs).sort_values(by='Percentage', ascending=False)
df_luxury_purchase_expanded = pd.DataFrame(data_luxury_purchase_expanded).sort_values(by='Percentage', ascending=False)
df_mobility_preferences = pd.DataFrame(data_mobility_preferences).sort_values(by='Percentage', ascending=False)
df_transport_criteria = pd.DataFrame(data_transport_criteria).sort_values(by='Percentage', ascending=False)
df_porsche_spirituality = pd.DataFrame(data_porsche_spirituality).sort_values(by='Percentage', ascending=False)

# Dummy-Variable für Porsche and Spirituality
porsche_spirituality_dummy = [1] * 19 + [0] * 81  # Beispielhaft: 19 Personen sehen die Verbindung, 81 nicht
df_correlation = pd.DataFrame({
    'Porsche_Spirituality': porsche_spirituality_dummy,
    'Interest_in_Luxury_Goods': [28] * 19 + [28] * 81,
    'Purchase_Motive_Quality': [66] * 19 + [66] * 81,
    'Purchase_Motive_Comfort': [62] * 19 + [62] * 81,
    'Purchase_Motive_Technology': [50] * 19 + [50] * 81,
    'Purchase_Motive_Status_Symbol': [45] * 19 + [45] * 81,
    'Purchase_Motive_Brand_Image': [60] * 19 + [60] * 81,
    'Purchase_Motive_Design': [55] * 19 + [55] * 81,
    'Purchase_Motive_Exclusivity': [40] * 19 + [40] * 81,
    'Purchase_Motive_Investment_Value': [35] * 19 + [35] * 81,
    'Purchase_Motive_Customer_Service': [30] * 19 + [30] * 81,
    'Purchase_Motive_Sustainability': [25] * 19 + [25] * 81,
    'Purchase_Motive_Performance': [70] * 19 + [70] * 81,
    'Purchase_Motive_Safety': [65] * 19 + [65] * 81,
    'Purchase_Motive_Heritage': [55] * 19 + [55] * 81,
})

# Korrelationen berechnen
correlation_matrix = df_correlation.corr()

# Stil für die Diagramme festlegen
sns.set(style="whitegrid")

st.title("Survey Results")

# Plot 1: Values and Beliefs
st.subheader('Values and Beliefs')
plt.figure(figsize=(12, 7))
sns.barplot(x='Percentage', y='Category', data=df_values_beliefs, palette="viridis")
plt.title('Values and Beliefs', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x')
st.pyplot(plt.gcf())

# Plot 2: Luxury Purchase Decisions
st.subheader('Luxury Purchase Decisions')
plt.figure(figsize=(12, 7))
sns.barplot(x='Percentage', y='Category', data=df_luxury_purchase_expanded, palette="plasma")
plt.title('Luxury Purchase Decisions', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x')
st.pyplot(plt.gcf())

# Plot 3: Mobility Preferences and Transport Criteria
st.subheader('Mobility Preferences and Transport Criteria')
plt.figure(figsize=(12, 7))

# Combine the two datasets for better visualization
df_combined = pd.concat([df_mobility_preferences, df_transport_criteria])
df_combined['Type'] = ['Mobility Preferences'] * len(df_mobility_preferences) + ['Transport Criteria'] * len(df_transport_criteria)

sns.barplot(x='Percentage', y='Category', hue='Type', data=df_combined, palette=["#3498db", "#e74c3c"])
plt.title('Mobility Preferences and Transport Criteria', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Type', loc='upper right')
plt.grid(axis='x')
st.pyplot(plt.gcf())

# Plot 4: Connection between Porsche and Spirituality
st.subheader('Connection between Porsche and Spirituality')
plt.figure(figsize=(12, 7))
sns.barplot(x='Percentage', y='Category', data=df_porsche_spirituality, palette="magma")
plt.title('Connection between Porsche and Spirituality', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x')
st.pyplot(plt.gcf())

# Plot 5: Correlation Matrix
st.subheader('Correlation Matrix between Porsche and Spirituality and Other Factors')
plt.figure(figsize=(12, 7))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, cbar_kws={'label': 'Correlation Coefficient'})
plt.title('Correlation Matrix', fontsize=16)
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)
st.pyplot(plt.gcf())
