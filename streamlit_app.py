import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data based on the provided information
data_values_beliefs = {
    'Category': ['Spirituality', 'Life Balance', 'Environmental Sustainability', 'Financial Prosperity', 'Relationships'],
    'Percentage': [20, 81, 8, 43, 86]
}

data_luxury_purchase = {
    'Category': ['Interest in Luxury Goods', 'Purchase Motive: Quality', 'Purchase Motive: Comfort', 'Brand Preference: Porsche', 'Brand Preference: Ferrari', 'Brand Preference: Lamborghini'],
    'Percentage': [28, 66, 62, 53, 53, 53]
}

data_mobility_preferences = {
    'Category': ['Use of Public Transport', 'Car Usage', 'Air Travel', 'Bicycle Usage', 'Car Sharing', 'Transport Criteria: Convenience', 'Transport Criteria: Practicality'],
    'Percentage': [38, 45, 23, 15, 5, 62, 68]
}

data_porsche_spirituality = {
    'Category': ['Porsche and Spirituality: Yes', 'Porsche and Spirituality: No'],
    'Percentage': [19, 81]
}

# Create DataFrames
df_values_beliefs = pd.DataFrame(data_values_beliefs)
df_luxury_purchase = pd.DataFrame(data_luxury_purchase)
df_mobility_preferences = pd.DataFrame(data_mobility_preferences)
df_porsche_spirituality = pd.DataFrame(data_porsche_spirituality)

# Set style for the plots
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
