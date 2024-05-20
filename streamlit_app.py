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

# Define colors (complementary and matching colors)
colors = [
    "#EBD698",  # Light gold
    "#000000",  # Black
    "#B12B28",  # Deep red
    "#D3B88C",  # Lighter gold
    "#555555",  # Dark gray
    "#E57373",  # Light red
    "#F4E1A1",  # Pale gold
    "#333333",  # Dark gray
    "#8E1D1A"   # Dark red
]

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add a white circle at the center to make it look like a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Title
plt.title('Respondents\' Views on Various Aspects', pad=20)

# Display the pie chart in Streamlit
st.pyplot(fig)
