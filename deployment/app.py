import streamlit as st
from predictor import predict_score

st.set_page_config(page_title="Anime Score Predictor", layout="centered")

st.title("🎌 Anime Score Predictor")
st.write("Fill out the details below and get a predicted MAL score!")

# --- Form inputs ---
with st.form("anime_form"):
    type_ = st.selectbox("Type", ["TV", "Movie", "ONA", "OVA", "Special"])
    status = st.selectbox("Status", ["Currently Airing", "Finished Airing"])
    season = st.selectbox("Season", ["Spring", "Summer", "Fall", "Winter", "None"])
    genres = st.multiselect("Genres", [
        "Action", "Adventure", "Avant Garde", "Award Winning", "Boys Love", "Cars", "Comedy", "Demons",
        "Drama", "Ecchi", "Erotica", "Fantasy", "Game", "Girls Love", "Gourmet", "Harem", "Hentai",
        "Historical", "Horror", "Josei", "Kids", "Martial Arts", "Mecha", "Military", "Music", "Mystery",
        "Parody", "Police", "Psychological", "Romance", "Samurai", "School", "Sci-Fi", "Seinen",
        "Shoujo", "Shounen", "Slice of Life", "Space", "Sports", "Super Power", "Supernatural",
        "Suspense", "Vampire", "Work Life"
    ])
    release_year = st.number_input("Release Year", min_value=1950, max_value=2030, value=2020)
    duration = st.number_input("Duration (in days: from first to last air date)", min_value=1)
    num_episodes = st.number_input("Number of Episodes", min_value=1, max_value=10000, value=12)
    studio_rank_score = st.slider("Studio Rank Score", 0.0, 1.0, 0.7, step=0.01)
    start_month = st.selectbox("Start Month", list(range(1, 13)))

    submitted = st.form_submit_button("Predict Score")

# --- Prediction logic ---
if submitted:
    user_input = {
        "type": type_,
        "status": status,
        "season": season,
        "genre": genres,
        "release_year": release_year,
        "duration": duration,
        "num_episodes": num_episodes,
        "studio_rank_score": studio_rank_score,
        "start_month": start_month
    }

    prediction = predict_score(user_input)
    st.success(f"Predicted Score: **{prediction:.2f}**")
