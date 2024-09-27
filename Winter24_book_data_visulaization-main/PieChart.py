import pandas as pd
import plotly.express as px

# Load the Excel file
df = pd.read_excel('fdb_more_properties.xlsx')

# Count occurrences of each value in the 'number_of_aromatic_rings' column
aromatic_counts = df['number_of_aromatic_rings'].value_counts()

# Calculate percentage of aromatic and non-aromatic molecules
total_molecules = len(df)
aromatic_percentage = (aromatic_counts[aromatic_counts.index > 0].sum() / total_molecules) * 100
non_aromatic_percentage = (aromatic_counts.get(0, 0) / total_molecules) * 100

# Create a pie chart
fig = px.pie(
    values=[non_aromatic_percentage, aromatic_percentage],
    names=['Non-Aromatic', 'Aromatic'],
    labels={'label', 'value'},
    title='Percentage of Aromatic and Non-Aromatic Molecules'
)

fig.show()
