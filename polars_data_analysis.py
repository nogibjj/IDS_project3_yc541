import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset using polars with ignore_errors and null_values parameters
df_spotify_polars = pl.read_csv(
    "spotify-2023.csv", 
    encoding="ISO-8859-1", 
    ignore_errors=True, 
    null_values=["BPM110KeyAModeMajorDanceability53Valence75Energy69Acousticness7Instrumentalness0Liveness17Speechiness3"]
)

# Display the first few rows of the dataset
print("=== Dataset Overview ===")
print(df_spotify_polars.head())
print("\n")

# Generate summary statistics for numeric columns
#print("testing1111")
#print(df_spotify_polars.describe().columns)
#summary_statistics_polars = df_spotify_polars.describe().select(['column', 'mean', '50%', 'std_dev'])
# First get the described DataFrame
df_described = df_spotify_polars.describe()

# Now, filter and select columns from this described DataFrame
summary_statistics_polars = df_described.filter(df_described['describe'].is_in(['mean', '50%', 'std_dev'])).select(['describe', 'streams'])

print("=== Summary Statistics ===")
print(summary_statistics_polars)
print("\n")

# Top 10 songs by streams
top_10_songs_polars = df_spotify_polars.sort("streams").reverse().limit(10)

print("=== Top 10 Songs by Streams ===")
print(top_10_songs_polars.select(['track_name', 'artist(s)_name', 'streams']))
print("\n")

# Convert the polars DataFrame to pandas for visualization
top_10_songs_pd = top_10_songs_polars.to_pandas()

# Data visualization
sns.set_style("whitegrid")
plt.figure(figsize=(12, 8))
sns.barplot(data=top_10_songs_pd, y='track_name', x='streams', hue='artist(s)_name', dodge=False, palette='muted')
plt.title('Top 10 Songs by Streams in Spotify 2023')
plt.xlabel('Number of Streams')
plt.ylabel('Track Name')
plt.legend(title='Artist(s)', loc='lower right')
plt.tight_layout()
plt.savefig("top_10_songs_spotify_2023.png")
plt.show()

