import gzip
import pandas as pd

# Define diiferent dtypes
title_ratings_dtype = {
    'tconst': 'object',
    'averageRating': 'float64',
    'numVotes': 'int64',
}

title_basics_dtype = {
    'tconst' : 'object',
    'titleType' : 'object',
    'primaryTitle' : 'object',
    'originalTitle' : 'object',
    'isAdult' : 'object',
    'startYear' : 'object',
    'endYear' : 'object',
    'runtimeMinutes' : 'object',
    'genres' : 'object',
}

title_akas_dtype = {
    'titleId' : 'object',
    'ordering' : 'int64',
    'title' : 'object',
    'region' : 'object',
    'language' : 'object',
    'types' : 'object',
    'attributes' : 'object',
    'isOriginalTitle' : 'int64',
}

# Specify the path to your gzipped TSV file
title_ratings_tsv_gz = r'C:\Users\Radic\OneDrive\Documents\Production\moviereccomendations\datasets\title.ratings.tsv.gz'
title_basics_tsv_gz = r'C:\Users\Radic\OneDrive\Documents\Production\moviereccomendations\datasets\title.basics.tsv.gz'
title_akas_tsv_gz = r'C:\Users\Radic\OneDrive\Documents\Production\moviereccomendations\datasets\title.akas.tsv.gz'

# Open and read the gzipped TSV file
with gzip.open(title_ratings_tsv_gz, 'rt', encoding='utf-8') as a:
    # Read the TSV file into a pandas DataFrame
    title_ratings_dataframe = pd.read_csv(a, sep='\t', dtype = title_ratings_dtype)

with gzip.open(title_basics_tsv_gz, 'rt', encoding='utf-8') as b:
    title_basics_dataframe = pd.read_csv(b, sep='\t', dtype = title_basics_dtype)

with gzip.open(title_akas_tsv_gz, 'rt', encoding='utf-8') as c:
    title_akas_dataframe = pd.read_csv(c, sep='\t', dtype = title_akas_dtype)

# Display the first few rows of the DataFrame
print(title_ratings_dataframe.head())
print(title_ratings_dataframe.dtypes)

print(title_basics_dataframe.head())
print(title_basics_dataframe.dtypes)

print(title_akas_dataframe.head())
print(title_akas_dataframe.dtypes)

# Optionally, save the DataFrame to a CSV file for further use
title_ratings_dataframe.to_csv('title_ratings.csv', index=False)
title_basics_dataframe.to_csv('title_basics.csv', index=False)
title_akas_dataframe.to_csv('title_akas.csv', index=False)
