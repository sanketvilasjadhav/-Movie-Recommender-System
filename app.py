import streamlit as st
import requests

# TMDB API credentials
API_KEY = "08b345f22c16c19f9c4fc5c2844c4135"
READ_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwOGIzNDVmMjJjMTZjMTlmOWM0ZmM1YzI4NDRjNDEzNSIsIm5iZiI6MTc1NDI5NjgzMi41MDgsInN1YiI6IjY4OTA3MjAwNzIxNjVkNmIwZWYzZTdkYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.VeC6WrpICirsVe8H6gBrhAWOg92-8RGoHu72tqjnnyY"

# TMDB API header
headers = {
    "Authorization": f"Bearer {READ_ACCESS_TOKEN}",
    "Content-Type": "application/json;charset=utf-8"
}

# Streamlit UI
st.title('🎬 Movie Recommender System')

# Hardcoded movie list
movie_list = [
    'Avatar',
    "Pirates of the Caribbean: At World's End",
    'Spectre',
    'The Dark Knight Rises',
    'John Carter',
    'Spider-Man 3',
    'Tangled',
    'Avengers: Age of Ultron',
    'Harry Potter and the Half-Blood Prince',
    'Batman v Superman: Dawn of Justice',
    'Superman Returns',
    'Quantum of Solace',
    "Pirates of the Caribbean: Dead Man's Chest",
    'The Lone Ranger',
    'Man of Steel',
    'The Chronicles of Narnia: Prince Caspian',
    'The Avengers',
    'Pirates of the Caribbean: On Stranger Tides',
    'Men in Black 3',
    'The Hobbit: The Battle of the Five Armies',
    'The Amazing Spider-Man',
    'Robin Hood',
    'The Hobbit: The Desolation of Smaug',
    'The Golden Compass',
    'King Kong',
    'Titanic',
    'Captain America: Civil War',
    'Battleship',
    'Jurassic World',
    'Skyfall',
    'Spider-Man 2',
    'Iron Man 3',
    'Alice in Wonderland',
    'X-Men: The Last Stand',
    'Monsters University',
    'Transformers: Revenge of the Fallen',
    'Transformers: Age of Extinction',
    'Oz: The Great and Powerful',
    'The Amazing Spider-Man 2',
    'TRON: Legacy',
    'Cars 2',
    'Green Lantern',
    'Toy Story 3',
    'Terminator Salvation',
    'Furious 7',
    'World War Z',
    'X-Men: Days of Future Past',
    'Star Trek Into Darkness',
    'Jack the Giant Slayer',
    'The Great Gatsby',
    'Prince of Persia: The Sands of Time',
    'Pacific Rim',
    'Transformers: Dark of the Moon',
    'Indiana Jones and the Kingdom of the Crystal Skull',
    'The Good Dinosaur',
    'Brave',
    'Star Trek Beyond',
    'WALL·E',
    'Rush Hour 3',
    'A Christmas Carol'
]

# Dropdown menu
selected_movie = st.selectbox("📽️ Choose a movie you like:", movie_list)

# TMDB movie poster fetch function
def fetch_poster(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&api_key={API_KEY}"
    response = requests.get(url, headers=headers)
    data = response.json()
    if data["results"]:
        poster_path = data["results"][0]["poster_path"]
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    else:
        return "https://via.placeholder.com/500x750?text=Poster+Not+Found"

# Dummy recommendation function (can be replaced with ML model)
def recommend_movies(movie):
    index = movie_list.index(movie)
    # Return next 5 movies (simple logic)
    recommended = movie_list[index+1:index+6] if index+6 <= len(movie_list) else movie_list[:5]
    return recommended

# Show recommendations
if st.button("🎯 Recommend Similar Movies"):
    st.subheader("🎉 Top Recommendations for You:")

    recommended_movies = recommend_movies(selected_movie)

    for i, rec_movie in enumerate(recommended_movies, start=1):
        poster_url = fetch_poster(rec_movie)
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(poster_url, width=150)
        with col2:
            st.markdown(f"**{i}. {rec_movie}**")
        st.markdown("---")
