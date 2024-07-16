import pandas as pd

data = pd.read_csv('super_data.csv', low_memory = False)

# Fill Missing Values
data['startYear'] = pd.to_numeric(data['startYear'], errors='coerce')
data['numVotes'] = pd.to_numeric(data['numVotes'], errors='coerce')
data['averageRating'] = pd.to_numeric(data['averageRating'], errors='coerce')
data = data.dropna(subset=['startYear', 'numVotes', 'averageRating'])

# Convert startYear to Int
data['startYear'] = data['startYear'].astype(int)

# Allow user input for year range and genre
start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))
selected_genre = input("Select from any of the following genres:\nAction, Adult, Adventure, Animation, Biography, Comedy, Crime, Documentary, Drama, Family, Fantasy, Film-Noir, Game-Show, History, Horror, Music, Musical, Mystery, News, Reality-TV, Romance, Sci-Fi, Sport, Talk-Show, Thriller, War, Western\nEnter the genre: ").lower()

# Filter Movies Based on User Input
filtered_data = data[(data['startYear'] >= start_year)
				& (data['startYear'] <= end_year)
				& (data['genres'].str.contains(selected_genre, case = False, na = False))]

sorted_data = filtered_data.sort_values(by = 'numVotes', ascending = False)

# Display the top recommendations
top_recommendations = sorted_data[['primaryTitle', 'startYear', 'genres', 'averageRating', 'numVotes']].head(10)
print("\nTop Movie Recommendations:")
print(top_recommendations)