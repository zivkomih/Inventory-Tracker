import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Beispiel-Daten basierend auf den bereitgestellten Informationen
data_values_beliefs = {
    'Category': ['Spirituality', 'Life Balance', 'Environmental Sustainability', 'Financial Prosperity', 'Relationships'],
    'Percentage': [20, 81, 8, 43, 86]
}

data_luxury_purchase = {
    'Category': ['Interest in Luxury Goods', 'Purchase Motive: Quality', 'Purchase Motive: Comfort', 'Purchase Motive: Technology', 'Purchase Motive: Status Symbol'],
    'Percentage': [28, 66, 62, 50, 45]
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
df_luxury_purchase = pd.DataFrame(data_luxury_purchase).sort_values(by='Percentage', ascending=False)
df_mobility_preferences = pd.DataFrame(data_mobility_preferences).sort_values(by='Percentage', ascending=False)
df_transport_criteria = pd.DataFrame(data_transport_criteria).sort_values(by='Percentage', ascending=False)
df_porsche_spirituality = pd.DataFrame(data_porsche_spirituality).sort_values(by='Percentage', ascending=False)

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
sns.barplot(x='Percentage', y='Category', data=df_luxury_purchase, palette="plasma")
plt.title('Luxury Purchase Decisions', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x')
st.pyplot(plt.gcf())

# Plot 3: Mobility Preferences
st.subheader('Mobility Preferences')
plt.figure(figsize=(12, 7))
sns.barplot(x='Percentage', y='Category', data=df_mobility_preferences, palette="cubehelix")
plt.title('Mobility Preferences', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x')
st.pyplot(plt.gcf())

# Plot 4: Transport Criteria
st.subheader('Transport Criteria')
plt.figure(figsize=(12, 7))
sns.barplot(x='Percentage', y='Category', data=df_transport_criteria, palette="cubehelix")
plt.title('Transport Criteria', fontsize=16)
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='x')
st.pyplot(plt.gcf())

# Plot 5: Connection between Porsche and Spirituality
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
