from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from Model import recommend_book , recommend_books



app = Flask(__name__)

# Load the books data


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    book_name = request.form['user_input']
    recommendations = recommend_books(book_name)
    return render_template('recommendation.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
