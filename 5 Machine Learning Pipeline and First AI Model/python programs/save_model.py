import pandas as pd
import os
import joblib

from sklearn.linear_model import LinearRegression

# -------------------------------
# PATH
current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

data_path = os.path.join(week5_dir, "datasets", "student_performance_encoded.csv")
model_path = os.path.join(week5_dir, "outputs", "student_model.pkl")

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
# TRAIN MODEL

model = LinearRegression()
model.fit(X, y)

# -------------------------------
# SAVE MODEL

joblib.dump(model, model_path)

print("Model saved at:", model_path)