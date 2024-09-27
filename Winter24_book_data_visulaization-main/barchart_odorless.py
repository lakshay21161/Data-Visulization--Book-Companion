import pandas as pd
import plotly.express as px

# Read the Excel file
df = pd.read_excel('fdb_molecules.xlsx')

# Filter the DataFrame to only include rows where 'fooddb_flavor_profile' is 'odorless'
odorless_df = df[df['fooddb_flavor_profile'] == 'odorless']

# Extract all functional groups from each cell in the 'functional_groups' column
odorless_df['functional_groups'] = odorless_df['functional_groups'].apply(lambda x: [group.strip() for group in x.replace(' or ', '@').split('@')] if isinstance(x, str) else [])

# Explode the lists of functional groups into separate rows
odorless_df = odorless_df.explode('functional_groups')

# Drop rows where the functional group couldn't be extracted (due to empty lists)
odorless_df = odorless_df[odorless_df['functional_groups'] != '']

# Count the occurrences of each functional group
functional_group_counts = odorless_df['functional_groups'].value_counts().to_dict()

# Create a bar chart using Plotly
fig = px.bar(x=list(functional_group_counts.keys()), y=list(functional_group_counts.values()), color=list(functional_group_counts.keys()),
             labels={'x': 'Functional Group', 'y': 'Count'}, title='Functional Group Counts for "Odorless" FoodDB Flavor Profiles')
fig.update_xaxes(tickangle=45)  # Rotate x-axis labels for better readability
fig.show()
