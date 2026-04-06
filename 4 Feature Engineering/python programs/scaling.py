import pandas as pd
import os
from sklearn.preprocessing import StandardScaler

# -------------------------------
# PATH SETUP
current_dir = os.path.dirname(__file__)
week4_dir = os.path.abspath(os.path.join(current_dir, ".."))

input_path = os.path.join(week4_dir, "datasets", "student_performance_encoded.csv")
output_path = os.path.join(week4_dir, "datasets", "student_performance_scaled.csv")

# -------------------------------
# LOAD DATA
data = pd.read_csv(input_path)

print("\nScaling Started\n")

# -------------------------------
# SELECT NUMERIC COLUMNS

numeric_cols = [
    "Study_Hours_per_Day",
    "Attendance_Percentage",
    "Previous_Exam_Score",
    "Final_Exam_Score",
    "Study_Efficiency",
    "Score_Improvement"
]

# -------------------------------
# APPLY SCALING

scaler = StandardScaler()
data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

# -------------------------------
# PREVIEW

print(data.head())

# -------------------------------
# SAVE DATA

data.to_csv(output_path, index=False)

print("\nScaled dataset saved at:", output_path)
print("Feature Scaling Completed ✅")