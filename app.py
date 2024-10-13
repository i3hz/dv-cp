from flask import Flask, render_template, request,redirect,url_for
import pandas as pd
from dvcp2 import get_recommendations, cosine_sim2, df2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie = request.form['movie']
    movie =movie.title()
    try:
        recommendations = get_recommendations(movie, cosine_sim2)
        return redirect(url_for('results', movie=movie))
    except KeyError:
        return redirect(url_for('results', movie=movie, error="Movie not found in the database"))

@app.route('/results')
def results():
    movie = request.args.get('movie')
    error = request.args.get('error')
    recommendations = []
    if movie:
        try:
            recommendations = get_recommendations(movie, cosine_sim2)
        except Exception as E:
            error = f"Movie '{movie}' not found in the database"
    
    return render_template('index.html', movie=movie, recommendations=recommendations, error=error)
if __name__ == '__main__':
    app.run(debug=True)
