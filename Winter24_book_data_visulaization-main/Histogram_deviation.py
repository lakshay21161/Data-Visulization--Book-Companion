import pandas as pd
import plotly.express as px

# Load the Excel file
df = pd.read_excel('fdb_more_properties.xlsx')

# Calculate expected number of aromatic bonds based on the number of aromatic rings
df['expected_aromatic_bonds'] = df['number_of_aromatic_rings'] * 6

# Calculate deviation from the expected number of aromatic bonds
df['deviation'] = df['number_of_aromatic_bonds'] - df['expected_aromatic_bonds']

# Filter out molecules with zero deviation
df_filtered = df[df['deviation'] != 0]

# Group by the number of aromatic rings and count the deviations
deviation_counts = df_filtered.groupby('number_of_aromatic_rings').size().reset_index(name='count')

# Plot the histogram using Plotly
fig = px.bar(deviation_counts, x='number_of_aromatic_rings', y='count',
             labels={'number_of_aromatic_rings': 'Number of Aromatic Rings', 'count': 'Deviation Counts'},
             title='Deviation Counts by Number of Aromatic Rings')

fig.show()
