import streamlit as st
import pickle

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movies_index = movies[movies['title'].values == movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
             
    return recommended_movies    


movies_list = movies['title'].values

st.title("Movie Recomender System")

option = st.selectbox(
    "How would you like to be contacted?",
    (movies_list),
)

st.write("You selected:", option)

if st.button("Recommend"):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)