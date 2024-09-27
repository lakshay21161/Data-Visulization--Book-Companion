import pandas as pd
import plotly.graph_objects as go

# Load the Excel file
df = pd.read_excel('fdb_molecules.xlsx')

# Assuming the column is named 'flavor_profile'
# Split the 'flavor_profile' column, explode into individual flavors, and count occurrences
flavor_counts = df['flavor_profile'].str.split('@').explode().value_counts()

# Now, flavor_counts is a Series with flavors as index and counts as values
# Select the top 20 most frequent flavors
top_20_flavors = flavor_counts.head(20)

# Define colors for the bars
colors = ['rgb(255, 0, 0)', 'rgb(0, 255, 0)', 'rgb(0, 0, 255)', 'rgb(255, 255, 0)', 'rgb(255, 0, 255)',
          'rgb(0, 255, 255)', 'rgb(128, 0, 0)', 'rgb(0, 128, 0)', 'rgb(0, 0, 128)', 'rgb(128, 128, 0)',
          'rgb(128, 0, 128)', 'rgb(0, 128, 128)', 'rgb(255, 128, 0)', 'rgb(255, 0, 128)', 'rgb(0, 255, 128)',
          'rgb(128, 255, 0)', 'rgb(0, 128, 255)', 'rgb(128, 0, 255)', 'rgb(255, 128, 128)', 'rgb(128, 255, 128)']

# Create a bar chart
fig = go.Figure(go.Bar(
    x=top_20_flavors.values,  # Frequency of flavors
    y=top_20_flavors.index,   # Flavor names
    orientation='h',          # Horizontal bars
    marker_color=colors       # Use predefined colors for the bars
))

# Update layout for a clean look
fig.update_layout(
    title='Top 20 Most Occurring Flavors',
    xaxis_title='Frequency',
    yaxis_title='Flavor',
    yaxis=dict(categoryorder='total ascending'),  # Sort bars by frequency
)

fig.show()
