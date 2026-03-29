"""
WEEK 6 — HYPERPARAMETER TUNING

Purpose:
- Best model configuration find karvu

What we learn:
- Model optimization
- Grid Search
"""

import pandas as pd
import os

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor

# -------------------------------
# PATH

current_dir = os.path.dirname(__file__)
week6_dir = os.path.abspath(os.path.join(current_dir, ".."))

data_path = os.path.join(week6_dir, "datasets", "student_performance_encoded.csv")

# -------------------------------
# LOAD DATA

data = pd.read_csv(data_path)

features = [
    "Study_Hours_per_Day",
    "Attendance_Percentage",
    "Previous_Exam_Score"
]

X = data[features]
y = data["Final_Exam_Score"]

# -------------------------------
# SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# PARAM GRID

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [5, 10, None]
}

# -------------------------------
# GRID SEARCH

model = RandomForestRegressor(random_state=42)

grid = GridSearchCV(
    model,
    param_grid,
    cv=3,
    scoring="neg_mean_absolute_error"
)

grid.fit(X_train, y_train)

# -------------------------------
# BEST MODEL

print("\nBEST PARAMETERS:")
print(grid.best_params_)

print("\nBEST SCORE (MAE):")
print(-grid.best_score_)