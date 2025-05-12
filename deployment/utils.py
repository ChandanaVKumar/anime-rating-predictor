def encode_user_input(raw_input, feature_list):
    encoded_input = {}

    # 1. Handle one-hot categorical fields
    # 'type' is single-select
    for t in ['Movie', 'ONA', 'OVA', 'Special', 'TV']:
        key = f"type_{t}"
        encoded_input[key] = 1 if raw_input.get("type") == t else 0

    # 'status' is single-select
    for status in ['Currently Airing', 'Finished Airing']:
        key = f"status_{status}"
        encoded_input[key] = 1 if raw_input.get("status") == status else 0

    # 'season' is single-select
    for season in ['Fall', 'None', 'Spring', 'Summer', 'Winter']:
        key = f"season_{season}"
        encoded_input[key] = 1 if raw_input.get("season") == season else 0

    # 'genre' is multi-select
    selected_genres = raw_input.get("genre", [])
    for genre in [f.replace("genre_", "") for f in feature_list if f.startswith("genre_")]:
        key = f"genre_{genre}"
        encoded_input[key] = 1 if genre in selected_genres else 0

    # 2. Handle numeric fields directly
    for field in ["release_year", "duration", "num_episodes", "studio_rank_score"]:
        encoded_input[field] = raw_input.get(field, 0)

    # 3. Handle start_month one-hot
    selected_month = raw_input.get("start_month")
    for m in range(1, 13):
        key = f"start_month_{m}"
        encoded_input[key] = 1 if selected_month == m else 0

    return encoded_input
