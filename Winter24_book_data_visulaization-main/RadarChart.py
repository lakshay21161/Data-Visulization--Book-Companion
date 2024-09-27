import pandas as pd
import plotly.graph_objects as go

# Read the Excel file
df = pd.read_excel('fdb_molecules.xlsx')

# Extract all functional groups from each cell in the 'functional_groups' column
all_functional_groups = df['functional_groups'].str.split('@| or ')

# Flatten the list of lists and remove NaN values
all_functional_groups = [group.strip() for sublist in all_functional_groups.dropna() for group in sublist]

# Count the occurrences of each functional group
functional_group_counts = pd.Series(all_functional_groups).value_counts().to_dict()

# Sort the functional group counts in descending order and get the top 10
top_10_functional_groups = dict(sorted(functional_group_counts.items(), key=lambda item: item[1], reverse=True)[:10])

# Extract labels and stats
labels = list(top_10_functional_groups.keys())
stats = list(top_10_functional_groups.values())

# Create a radar chart
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=stats + stats[:1],
      theta=labels + [labels[0]],
      fill='toself',
      name='Top 10 Functional Groups'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, max(stats)]
    )),
  showlegend=True
)

fig.show()
