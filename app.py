import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=68d5b633713ed84db723332543ba33c4'.format(movie_id))
    data = response.json()

    # st.text(data)

    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters =[]

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

        # fatch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("MOVIE RECOMMENDER SYSTEM")

selected_movie_name = st.selectbox(
    'Movie Name', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.markdown(
    #         f'<a href="{'https://www.themoviedb.org/movie/65'}" target="_blank"><img src="{posters[0]}" style="max-width:100px; max-height:200px;"></a>',
    #         unsafe_allow_html=True)
    #     st.text(names[0])
    # with col2:
    #     st.markdown(
    #         f'<a href="{'https://www.themoviedb.org/movie/65'}" target="_blank"><img src="{posters[1]}" style="max-width:100px; max-height:200px;"></a>',
    #         unsafe_allow_html=True)
    #     st.text(names[1])
    # with col3:
    #     st.markdown(
    #         f'<a href="{'https://www.themoviedb.org/movie/65'}" target="_blank"><img src="{posters[2]}" style="max-width:100px; max-height:200px;"></a>',
    #         unsafe_allow_html=True)
    #     st.text(names[2])
    # with col4:
    #     st.markdown(
    #         f'<a href="{'https://www.themoviedb.org/movie/65'}" target="_blank"><img src="{posters[3]}" style="max-width:100px; max-height:200px;"></a>',
    #         unsafe_allow_html=True)
    #     st.text(names[3])
    # with col5:
    #     st.markdown(
    #         f'<a href="{'https://www.themoviedb.org/movie/65'}" target="_blank"><img src="{posters[4]}" style="max-width:100px; max-height:200px;"></a>',
    #         unsafe_allow_html=True)
    #     st.text(names[4])


    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

