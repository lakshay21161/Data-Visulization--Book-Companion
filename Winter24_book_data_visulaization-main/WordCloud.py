import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('fdb_molecules.xlsx')

# Assuming the column is named 'flavor_profile'
# Split the 'flavor_profile' column, explode into individual flavors, and count occurrences
flavor_counts = df['flavor_profile'].str.split('@').explode().value_counts()

# Now, flavor_counts is a Series with flavors as index and counts as values
# Convert to dictionary for the word cloud
all_flavors = flavor_counts.to_dict()

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(all_flavors)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axes
plt.show()
