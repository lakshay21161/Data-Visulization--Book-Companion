import pandas as pd
import plotly.graph_objects as go

#This plot helps in visualising a physical property of the molecules. 
#Each aromatic ring should ideally contribute 6 aromatic bonds

# Load the Excel file
df = pd.read_excel('fdb_more_properties.xlsx')

# Calculate expected number of aromatic bonds based on the number of aromatic rings
df['expected_aromatic_bonds'] = df['number_of_aromatic_rings'] * 6

# Calculate deviation from the expected number of aromatic bonds
df['deviation'] = df['number_of_aromatic_bonds'] - df['expected_aromatic_bonds']

# Define color scheme
expected_color = 'blue'  # Color for points following the expected pattern
deviation_color = 'red'  # Color for points deviating from the expected pattern

# Create a scatter plot
fig = go.Figure()

# Add markers for data points following the expected pattern
fig.add_trace(go.Scatter(
    x=df[df['deviation'] == 0]['number_of_aromatic_rings'],
    y=df[df['deviation'] == 0]['number_of_aromatic_bonds'],
    mode='markers',
    marker=dict(color=expected_color, size=10),
    name='Expected Pattern (Multiple of 6 Bonds)'
))

# Add markers for data points deviating from the expected pattern
deviation_points = df[df['deviation'] != 0]
if not deviation_points.empty:
    fig.add_trace(go.Scatter(
        x=deviation_points['number_of_aromatic_rings'],
        y=deviation_points['number_of_aromatic_bonds'],
        mode='markers',
        marker=dict(color=deviation_color, size=abs(deviation_points['deviation']) * 2),  # Increase marker size based on deviation
        name='Deviation from Expected Pattern'
    ))

# Customize layout
fig.update_layout(
    title='Relationship between Number of Aromatic Rings and Aromatic Bonds',
    xaxis_title='Number of Aromatic Rings',
    yaxis_title='Number of Aromatic Bonds',
)

fig.show()
