import pandas as pd
import plotly.express as px

# Load your Excel file into a DataFrame
df = pd.read_excel('fdb_more_properties.xlsx')  # Make sure to replace 'path_to_your_file.xlsx' with the actual path

# Ensure that the column name is correctly spelled as it appears in your file, including case sensitivity
# If your column name is 'pKa' instead of 'pka', adjust it accordingly
pka_values = df['pka']  # This will extract all values from the 'pka' column

# Now, create a box plot of the pKa values
fig = px.box(pka_values, title='Distribution of pKa Values', labels={'value': 'pKa'})  # Adjust label if necessary

# Show the plot
fig.show()
