"""
WEEK 6 — ADVANCED RANDOM FOREST (INDUSTRY LEVEL)

Purpose:
- Build production-style ML pipeline
- Improve accuracy using proper workflow

Includes:
✔ Pipeline
✔ Scaling
✔ Model training
✔ Evaluation
✔ Output saving
"""

import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# -------------------------------
# PATH SETUP

current_dir = os.path.dirname(__file__)
week6_dir = os.path.abspath(os.path.join(current_dir, ".."))

data_path = os.path.join(week6_dir, "datasets", "student_performance_encoded.csv")
output_path = os.path.join(week6_dir, "outputs", "advanced_rf_results.txt")

# -------------------------------
# LOAD DATA

data = pd.read_csv(data_path)

# -------------------------------
# FEATURE SELECTION

features = [
    "Study_Hours_per_Day",
    "Attendance_Percentage",
    "Previous_Exam_Score"
]

X = data[features]
y = data["Final_Exam_Score"]

# -------------------------------
# SPLIT DATA

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# PIPELINE (IMPORTANT 🔥)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42))
])

# -------------------------------
# TRAIN

pipeline.fit(X_train, y_train)

# -------------------------------
# PREDICT

pred = pipeline.predict(X_test)

# -------------------------------
# EVALUATE

mae = mean_absolute_error(y_test, pred)
r2 = r2_score(y_test, pred)

# -------------------------------
# OUTPUT

result = f"""
ADVANCED RANDOM FOREST RESULTS

MAE: {round(mae,2)}
R2 Score: {round(r2,2)}
"""

print(result)

# SAVE RESULT

with open(output_path, "w") as f:
    f.write(result)

print("Results saved at:", output_path)