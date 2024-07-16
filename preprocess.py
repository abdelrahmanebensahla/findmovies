import pandas as pd

# Load data
ratings = pd.read_csv('title_ratings.csv')
basics = pd.read_csv('title_basics.csv', low_memory = False)
akas = pd.read_csv('title_akas.csv')

# Uniform tconst Column
akas = akas.rename(columns = {'titleId' : 'tconst'})

# Merge Dataframes Under tconst
ratings_basics_merge = pd.merge(basics, ratings, on = 'tconst')
super_data = pd.merge(akas, ratings_basics_merge, on = 'tconst')

# Keep Original Titles
super_data = super_data[super_data['isOriginalTitle'] != 0]

# Filter to Only Movies
super_data = super_data[super_data['titleType'] == 'movie'] # Figure out if 'movie' is the keyword

# Drop Uneccessary Columns
super_data.drop(columns = ['ordering', 'title', 'language', 'types', 'attributes', 'isOriginalTitle', 'originalTitle', 'isAdult', 'titleType'], inplace = True)

# Swap Columns
cols = list(super_data.columns)
cols[1], cols[2] = cols[2], cols[1]
super_data = super_data[cols]

print(super_data.head())
print(super_data.columns)
print(super_data.info())

# Save to CSV
super_data.to_csv('find_movies/data/super_data.csv', index = False)




# Merge datasets
	# data = pd.merge(ratings, movies, on='movieId')

# Save processed data
	#data.to_csv('processed_data.csv', index=False)
