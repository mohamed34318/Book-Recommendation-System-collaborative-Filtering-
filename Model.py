import pickle
import numpy as np
import pandas as pd
import numpy as np
# Load the model from the .pkl file
with open('book_recommendation_model.pkl', 'rb') as file:
    model_data = pickle.load(file)

# Extract the components
similarity_score = model_data['similarity_score']
pt = model_data['pt']

# Now you can use the `recommend` function as before
def recommend_books(book_name):
    books = pd.read_csv('Data/books.csv')
    # Get the recommended book titles
    recommended_titles = recommend_book(book_name)
    
    # Fetch the book details from the dataset
    recommendations = []
    for title in recommended_titles:
        book_info = books[books['Book-Title'] == title].iloc[0]
        recommendations.append({
            'Book-Title': book_info['Book-Title'],
            'Publisher': book_info['Publisher'],
            'Image-URL-M': book_info['Image-URL-M']
        })
    
    return recommendations

def recommend_book(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]
    recommended_books = [pt.index[i[0]] for i in similar_items]
    return recommended_books