import numpy as np
import pickle
import json
from pathlib import Path
from utils import encode_user_input
import joblib

# Load model components only once
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model_data"

w = np.load(MODEL_DIR / "weights.npy")
b = np.load(MODEL_DIR / "bias.npy")

feature_scaler = joblib.load(MODEL_DIR / "feature_scaler.pkl")

target_scaler = joblib.load(MODEL_DIR / "target_scaler.pkl")

with open(MODEL_DIR / "feature_list.json", "r") as f:
    feature_list = json.load(f)


# def predict_score(raw_input):
#     user_input_dict = encode_user_input(raw_input, feature_list)
#
#     # Same code from earlier
#     x = np.zeros(len(feature_list))
#     for i, feature in enumerate(feature_list):
#         x[i] = user_input_dict.get(feature, 0)
#
#     x_scaled = feature_scaler.transform([x])
#     y_scaled_pred = np.dot(x_scaled, w) + b
#
#     y_pred = target_scaler.inverse_transform([[y_scaled_pred]])[0][0]
#     return float(y_pred)

def predict_score(raw_input):
    user_input_dict = encode_user_input(raw_input, feature_list)

    x = np.zeros(len(feature_list))
    for i, feature in enumerate(feature_list):
        x[i] = user_input_dict.get(feature, 0)

    # List of the 4 numeric columns you scaled during training
    numeric_cols = ['release_year', 'duration', 'num_episodes', 'studio_rank_score']

    # Get indices of these features
    numeric_indices = [feature_list.index(col) for col in numeric_cols]

    # Extract the 4 numeric values
    numeric_values = np.array([x[i] for i in numeric_indices]).reshape(1, -1)

    # Scale them
    scaled_numeric_values = feature_scaler.transform(numeric_values).flatten()

    # Put scaled values back into x
    for idx, val in zip(numeric_indices, scaled_numeric_values):
        x[idx] = val


    # y_scaled_pred = float(np.dot(x, w) + b)
    #
    # # Inverse transform target to get prediction in original scale
    # y_pred = target_scaler.inverse_transform(y_scaled_pred)[0][0]
    #
    # return y_pred

    y_scaled_pred = float(np.dot(x, w) + b)

    y_pred = target_scaler.inverse_transform(np.array([[y_scaled_pred]]))[0][0]
    return float(y_pred)
