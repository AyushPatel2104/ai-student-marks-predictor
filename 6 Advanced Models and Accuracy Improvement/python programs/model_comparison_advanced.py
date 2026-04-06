"""
WEEK 6 — MODEL COMPARISON (INDUSTRY LEVEL)

Purpose:
- Compare multiple models
- Decide best model based on metrics

Includes:
✔ Linear Regression
✔ Random Forest
✔ MAE comparison
✔ R2 comparison
✔ Output saving
"""

import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# -------------------------------
# PATH SETUP

current_dir = os.path.dirname(__file__)
week6_dir = os.path.abspath(os.path.join(current_dir, ".."))

data_path = os.path.join(week6_dir, "datasets", "student_performance_encoded.csv")
output_path = os.path.join(week6_dir, "outputs", "model_comparison.txt")

# -------------------------------
# LOAD DATA

data = pd.read_csv(data_path)

# -------------------------------
# FEATURES

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
# LINEAR REGRESSION

lr = LinearRegression()
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

lr_mae = mean_absolute_error(y_test, lr_pred)
lr_r2 = r2_score(y_test, lr_pred)

# -------------------------------
# RANDOM FOREST

rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_r2 = r2_score(y_test, rf_pred)

# -------------------------------
# RESULTS

result = f"""
MODEL COMPARISON RESULTS

Linear Regression:
MAE: {round(lr_mae,2)}
R2 Score: {round(lr_r2,2)}

Random Forest:
MAE: {round(rf_mae,2)}
R2 Score: {round(rf_r2,2)}
"""

print(result)

# -------------------------------
# BEST MODEL DECISION

if rf_mae < lr_mae:
    best = "Random Forest"
else:
    best = "Linear Regression"

print(f"Best Model: {best}")

# -------------------------------
# SAVE OUTPUT

with open(output_path, "w") as f:
    f.write(result + f"\nBest Model: {best}")

print("Results saved at:", output_path)