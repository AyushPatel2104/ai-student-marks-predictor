import joblib
import os
import numpy as np
import pandas as pd

print("\n🔹 WEEK 7 — CLI PREDICTION SYSTEM (SMART) 🔹\n")

# ---------------------------
# LOAD DATA (FOR RANGE INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "outputs", "clean_classification_data.csv")

df = pd.read_csv(data_path)

# ---------------------------
# LOAD MODEL

model_path = os.path.join(BASE_DIR, "..", "outputs", "models", "pipeline_model.pkl")

if not os.path.exists(model_path):
    print("❌ Model not found! Run pipeline_model.py first.")
    exit()

model = joblib.load(model_path)

print("✅ Model Loaded Successfully")

# ---------------------------
# FEATURE LIST (IMPORTANT)

features = [
    "Student_ID",
    "Age",
    "Study_Hours_per_Day",
    "Sleep_Hours",
    "Attendance_Percentage",
    "Assignments_Completed",
    "Previous_Exam_Score"
]

# ---------------------------
# SHOW RANGE INFO

print("\n📊 INPUT GUIDELINES (from dataset):\n")

for col in features:
    if col in df.columns:
        print(f"{col}: Min = {df[col].min()} | Max = {df[col].max()}")

# ---------------------------
# USER INPUT

try:
    study_hours = float(input("\nEnter Study Hours per Day: "))
    sleep_hours = float(input("Enter Sleep Hours: "))
    attendance = float(input("Enter Attendance Percentage: "))
    assignments = float(input("Enter Assignments Completed: "))
    previous_score = float(input("Enter Previous Exam Score: "))
    age = float(input("Enter Age: "))

except:
    print("❌ Invalid input! Please enter numeric values.")
    exit()

# ---------------------------
# SIMPLE VALIDATION (OPTIONAL)

if study_hours < 0 or study_hours > 24:
    print("⚠️ Study hours seems unrealistic!")

# ---------------------------
# CREATE INPUT DATAFRAME (FIXED)

input_df = pd.DataFrame([{
    "Student_ID": 0,
    "Age": age,
    "Study_Hours_per_Day": study_hours,
    "Sleep_Hours": sleep_hours,
    "Attendance_Percentage": attendance,
    "Assignments_Completed": assignments,
    "Previous_Exam_Score": previous_score
}])

# ---------------------------
# PREDICTION

prediction = model.predict(input_df) 

print("\n🎯 Predicted Performance:", prediction[0])

print("\n🚀 PREDICTION COMPLETED\n")