"""
WEEK 6 — FINAL OPTIMIZED MODEL

Purpose:
- Use best parameters
- Train final model
- Save for real usage

This is production-ready AI model
"""

import pandas as pd
import os
import joblib

from sklearn.ensemble import RandomForestRegressor

# -------------------------------
# PATH

current_dir = os.path.dirname(__file__)
week6_dir = os.path.abspath(os.path.join(current_dir, ".."))

data_path = os.path.join(week6_dir, "datasets", "student_performance_encoded.csv")
model_path = os.path.join(week6_dir, "outputs", "final_model.pkl")

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
# FINAL MODEL (USE BEST PARAMS)

model = RandomForestRegressor(
    n_estimators=200,   # from tuning
    max_depth=10,       # from tuning
    random_state=42
)

# -------------------------------
# TRAIN

model.fit(X, y)

# -------------------------------
# SAVE MODEL

joblib.dump(model, model_path)

print("\n🏆 FINAL MODEL TRAINED & SAVED")
print("Model path:", model_path)