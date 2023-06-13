import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Read the CSV file
df = pd.read_csv('output.csv')

# Perform data analysis
# Example: Clustering based on artist familiarity and artist hotttnesss
data = df[['artist_familiarity', 'artist_hotttnesss']]
data = data.fillna(data.mean())
kmeans = KMeans(n_clusters=3)  # Assuming we want 3 clusters
kmeans.fit(data)
labels = kmeans.labels_

# Visualize the clusters
plt.scatter(data['artist_familiarity'], data['artist_hotttnesss'], c=labels)
plt.xlabel('Artist Familiarity')
plt.ylabel('Artist Hotttnesss')
plt.title('Clustering of Artists')
plt.show()

# Perform statistical analysis
# Example: Calculate the p-value between artist familiarity and song hotttnesss
artist_familiarity = data['artist_familiarity']
song_hotttnesss = df['song_hotttnesss']
song_hotttnesss = song_hotttnesss.fillna(song_hotttnesss.mean())
# Calculate the Pearson correlation coefficient and p-value
correlation_coefficient, p_value = pearsonr(artist_familiarity, song_hotttnesss)

# Print the p-value
print('The p-value between artist familiarity and song hotttnesss is:', p_value)
