import streamlit as st
import matplotlib.pyplot as plt

# Data from the user's input
labels = [
    "Spirituality: Not important",
    "Spirituality: Strongly agree",
    "Self-perception: See as spiritual",
    "Self-perception: Disagree",
    "Balanced life: Very important",
    "Ecological sustainability: Prioritize",
    "Financial prosperity: Agree",
    "Meaningful relationships: Agree",
    "Personal development: Important"
]

sizes = [
    34,  # Spirituality: Not important
    4,   # Spirituality: Strongly agree
    19,  # Self-perception: See as spiritual
    36,  # Self-perception: Disagree
    81,  # Balanced life: Very important
    31,  # Ecological sustainability: Prioritize
    69,  # Financial prosperity: Agree
    86,  # Meaningful relationships: Agree
    79   # Personal development: Important
]

# Define colors (using the specified colors)
colors = [
    "#EBD698",  # Light gold
    "#000000",  # Black
    "#B12B28",  # Deep red
    "#EBD698",  # Light gold
    "#000000",  # Black
    "#B12B28",  # Deep red
    "#EBD698",  # Light gold
    "#000000",  # Black
    "#B12B28"   # Deep red
]

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Respondents\' Views on Various Aspects')

# Display the pie chart in Streamlit
st.pyplot(fig)

