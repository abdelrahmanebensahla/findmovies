from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load your data
data = pd.read_csv('data/super_data.csv', low_memory = False)

# Convert Data to Numeric AND Fill Missing Values
data['startYear'] = pd.to_numeric(data['startYear'], errors='coerce')
data['numVotes'] = pd.to_numeric(data['numVotes'], errors='coerce')
data['averageRating'] = pd.to_numeric(data['averageRating'], errors='coerce')
data = data.dropna(subset=['startYear', 'numVotes', 'averageRating'])
data['startYear'] = data['startYear'].astype(int)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form.get('genre')
    start_year = int(request.form.get('start_year'))
    end_year = int(request.form.get('end_year'))

    genre = genre.lower()

    print(f"Genre: {genre}, Start Year: {start_year}, End Year: {end_year}")

    recommendations = data[(data['genres'].str.contains(genre, case = False, na = False)) &
                         (data['startYear'] >= start_year) &
                         (data['startYear'] <= end_year)]

    sorted_recommendations = recommendations.sort_values(by = 'numVotes', ascending = False)

    top_recommendations = sorted_recommendations[['primaryTitle', 'startYear', 'genres', 'averageRating', 'numVotes']].head(10)

    top_recommendations_dict = top_recommendations.to_dict('records')

    return jsonify(top_recommendations_dict)

if __name__ == '__main__':
    app.run(debug = True)
