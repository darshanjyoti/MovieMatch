import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image

movies_dict = pickle.load(open('movieDict.pkl','rb'))

similarity = pickle.load(open('similarity.pkl','rb'))

movies = pd.DataFrame(movies_dict)
#st.subheader("MovieMatch: Your Personal Movie Recommender")
#st.text("Uncover Your Ideal Movies Based on Your Favorite Films and Preferences")
st.markdown(
    """
    <h2 style='color: #b00b5d;'>MovieMatch: Your Personal Movie Recommender</h2>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <h5 style='color: blue; font-family: "Montserrat", sans-serif; font-style: italic;'>Uncover Your Ideal Movies Based on Your Favorite Films and Preferences</h5>
    """,
    unsafe_allow_html=True
)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances [1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

selectedMovieName = st.selectbox(
    "Type or select a movie from the dropdown",
    (movies['title'].values))

st.write('You selected:', selectedMovieName)


if st.button('Show Recommendations'):
    recommended_movie_names,recommended_movie_posters = recommend(selectedMovieName)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.subheader(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.subheader(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.subheader(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.subheader(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.subheader(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
