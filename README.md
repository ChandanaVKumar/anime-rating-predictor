### 📊 Anime Rating Predictor — A Linear Regression Project

This project aims to predict anime ratings using a carefully preprocessed and feature-engineered dataset from MyAnimeList. I deliberately chose linear regression as the first model—not for its complexity, but for its transparency and interpretability. It forced me to truly understand each step of the machine learning pipeline: how to deal with multi-label categorical variables like genres and studios, how to scale features properly without causing data leakage, and how to evaluate trade-offs in target and feature selection.

Rather than relying on black-box models, this project helped me gain hands-on experience with real-world data challenges and build a solid foundation in core ML concepts.

---
## 📁 Project Structure

This project has been split into multiple Jupyter Notebooks for clarity and modularity. Each notebook focuses on a specific stage in the machine learning workflow:

- `1_data_cleaning_and_preprocessing_part1 to part5.ipynb`  
  These notebooks cover different stages of the data cleaning and preprocessing process, including:
  - Initial data inspection and cleanup
  - Handling missing values
  - Feature engineering
  - Final dataset preparation

- `2_eda_part1 and part2.ipynb`  
  Exploratory data analysis split into two parts:
  - Understanding distribution of key variables (genres, types, scores, popularity, etc.)
  - Identifying relationships and trends that may influence model performance

- `3_model_training_and_prediction.ipynb`  
The final notebook covers:
- Rationale behind target selection
- Training and evaluating the linear regression model
- Error analysis and final performance insights

**Note**: Multiple versions of the dataset have been stored in the `dataset/` folder, corresponding to different stages of cleaning and transformation.

---

### 🔍 Why This Project is More Than Just Linear Regression

Although this project uses linear regression as the core model, it is **far from a plug-and-play implementation**. The primary goal was to **build everything from scratch**, deeply understand the entire machine learning pipeline, and apply it to a non-trivial, categorical-heavy real-world dataset. Here's what makes it special:

#### ✅ From-Scratch Implementation of Linear Regression with Regularization

* Implemented **gradient descent manually** in NumPy, including **vectorized operations** for performance.
* Integrated **L2 regularization** (Ridge regression) directly into the gradient and cost function computation.
* **Tuned the regularization strength** (`lambda`) through experimentation to balance bias and variance.

#### 📊 Real-World Dataset with High Categorical Complexity

* Worked with a **non-numeric, noisy dataset** (anime metadata) not naturally suited for linear models.
* Preprocessed over **50 categorical features** using one-hot encoding, including `type`, `genre`, `status`, and `season`.
* Normalized numerical features to stabilize and accelerate gradient descent convergence.

#### 🧠 Thoughtful Feature Engineering & Analysis

* **Evaluated feature importance**, experimented with **removing correlated or redundant features** (like `start_month`).
* Assessed model performance using **train/dev splits**, **R² scores**, and **MSE** to monitor for overfitting.

#### 📉 Performance Optimization & Reflection

* Achieved stable generalization with **regularized weights** and **feature pruning**.
* Recognized limitations in the dataset/model fit (R² ≈ 0.25), showing maturity in knowing when to stop optimizing and focus on deployment.

---

## 🌐 **Access the Streamlit App**

Try the live Anime Rating Predictor app on Streamlit:

[**Anime Rating Predictor App**](https://anime-rating-predictor-nqjjmbkcrwg8ghptlwrien.streamlit.app/)

This link will take you directly to the app where you can interact with the model, upload data, and see predicted ratings without needing to run anything locally.

---
