import polars as pl

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
summary_statistics_polars = df_spotify_polars.describe().select(['column', 'mean', '50%', 'std_dev'])
summary_statistics_polars = summary_statistics_polars.with_column(
    summary_statistics_polars.col('std_dev').alias('Standard Deviation')
).select(['column', 'mean', '50%', 'Standard Deviation'])
print("=== Summary Statistics ===")
print(summary_statistics_polars)
print("\n")

# Top 10 songs by streams
top_10_songs_polars = df_spotify_polars.sort('streams', reverse=True).limit(10)
print("=== Top 10 Songs by Streams ===")
print(top_10_songs_polars.select(['track_name', 'artist(s)_name', 'streams']))
print("\n")
