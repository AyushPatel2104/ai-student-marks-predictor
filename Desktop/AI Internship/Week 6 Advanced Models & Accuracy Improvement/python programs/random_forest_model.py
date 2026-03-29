"""
WEEK 6 — RANDOM FOREST MODEL

Purpose:
- Linear model karta better prediction karvu
- Complex patterns samajva

What we learn:
- Advanced ML model
- Better accuracy
"""

import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# -------------------------------
# PATH SETUP

current_dir = os.path.dirname(__file__)
week6_dir = os.path.abspath(os.path.join(current_dir, ".."))

data_path = os.path.join(week6_dir, "datasets", "student_performance_encoded.csv")

# -------------------------------
# LOAD DATA

data = pd.read_csv(data_path)

# -------------------------------
# FEATURES (NO DATA LEAKAGE)

features = [
    "Study_Hours_per_Day",
    "Attendance_Percentage",
    "Previous_Exam_Score"
]

X = data[features]
y = data["Final_Exam_Score"]

# -------------------------------
# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# MODEL (RANDOM FOREST)

model = RandomForestRegressor(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

# -------------------------------
# PREDICTION

pred = model.predict(X_test)

# -------------------------------
# EVALUATION

mae = mean_absolute_error(y_test, pred)

print("\n🌳 RANDOM FOREST RESULTS")
print("---------------------------")
print("MAE:", round(mae, 2))
print("---------------------------")

output_path = os.path.join(week6_dir, "outputs", "rf_results.txt")

with open(output_path, "w") as f:
    f.write(f"Random Forest MAE: {round(mae,2)}")

print("Results saved at:", output_path)