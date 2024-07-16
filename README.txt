Overview
This project is a web-based movie recommendation system developed using Flask, pandas, and machine learning. The application allows users to receive personalized movie suggestions based on selected genres and year ranges, sorted by the highest number of votes. The web app features a user-friendly interface with validated inputs and is deployed on AWS Elastic Beanstalk, with logging and monitoring handled via AWS CloudWatch.

Features
Personalized Recommendations: Users can select a genre and specify a year range to receive tailored movie recommendations.
Data Processing: Utilizes pandas for data cleaning and preprocessing.
Machine Learning: Employs machine learning algorithms to sort and recommend movies based on user preferences.
User Interface: Clean and intuitive interface built with HTML, CSS, and JavaScript.
Deployment: Scalable and reliable deployment on AWS Elastic Beanstalk with monitoring via AWS CloudWatch.

Installation
Clone the repository:
gh repo clone abdelrahmanebensahla/findmovies

Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the dependencies:
pip install -r requirements.txt

Download IMDB's Data HERE:
https://datasets.imdbws.com/
	title.akas.tsv.gz
	title.basics.tsv.gz
	title.ratings.tsv.gz
		THEN PLACE IN FOLDER "datasets"


Run:
py data_unzip.py
py preprocess.py
py query.py (OPTIONAL: runs app in shell)
cd find_movies
py app.py

Open your web browser and go to:
http://127.0.0.1:5000/

Usage
Select a genre from the drop-down menu.
Enter the start and end year range.
Click "Get Recommendations" to view the top recommended movies based on the number of votes.

Project Structure
app.py: Main Flask application file.
templates/index.html: HTML file for the frontend.
static/style.css: CSS file for styling the frontend.
data/your_data_file.csv: CSV file containing movie data.

Deployment
The application is deployed on AWS Elastic Beanstalk. Ensure you have an AWS account and the AWS CLI configured. Use the following command to deploy:
eb init -p python-3.7 movie-recommendation-app
eb create findmovies-env

Contributing
Feel free to submit issues and pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. See the LICENSE file for details.