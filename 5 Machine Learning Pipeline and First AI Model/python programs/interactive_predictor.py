import joblib
import os
import pandas as pd

# -------------------------------
# PATH
current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

model_path = os.path.join(week5_dir, "outputs", "student_model.pkl")

# -------------------------------
# LOAD MODEL
model = joblib.load(model_path)

print("\n🎯 AI Student Score Predictor\n")

# -------------------------------
# USER INPUT

study_hours = float(input("Enter Study Hours per Day: "))
attendance = float(input("Enter Attendance Percentage: "))
previous_score = float(input("Enter Previous Exam Score: "))

# -------------------------------
# CREATE DATAFRAME

sample = pd.DataFrame({
    "Study_Hours_per_Day": [study_hours],
    "Attendance_Percentage": [attendance],
    "Previous_Exam_Score": [previous_score]
})

# -------------------------------
# PREDICT

prediction = model.predict(sample)

# -------------------------------
# OUTPUT

print("\n📊 RESULT")
print("---------------------------")
print(f"Input:")
print(f"Study Hours = {study_hours}")
print(f"Attendance = {attendance}")
print(f"Previous Score = {previous_score}")

print("\nPredicted Final Score:", round(prediction[0], 2))
print("---------------------------")