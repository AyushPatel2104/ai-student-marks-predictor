import pandas as pd
import os
from sklearn.linear_model import LinearRegression

# -------------------------------
# PATH
current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

data_path = os.path.join(week5_dir, "datasets", "student_performance_encoded.csv")

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
# MODEL

model = LinearRegression()
model.fit(X, y)

# -------------------------------
# FEATURE IMPORTANCE

importance = model.coef_

result = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

print("\nFeature Importance:\n")
print(result.sort_values(by="Importance", ascending=False))