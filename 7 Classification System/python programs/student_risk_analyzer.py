import joblib
import os
import pandas as pd

print("\n🔹 STUDENT RISK ANALYZER 🔹\n")

# ---------------------------
# LOAD MODEL

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "..", "outputs", "models", "pipeline_model.pkl")

model = joblib.load(model_path)

print("✅ Model Loaded")

# ---------------------------
# USER INPUT

try:
    study_hours = float(input("Enter Study Hours: "))
    sleep_hours = float(input("Enter Sleep Hours: "))
    attendance = float(input("Enter Attendance %: "))
    assignments = float(input("Enter Assignments Completed: "))
    previous_score = float(input("Enter Previous Score: "))
    age = float(input("Enter Age: "))
except:
    print("❌ Invalid input")
    exit()

# ---------------------------
# CREATE DATAFRAME

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

prediction = model.predict(input_df)[0]

# ---------------------------
# RISK LOGIC

def risk_level(performance):
    if performance == "Excellent":
        return "Low Risk"
    elif performance == "Good":
        return "Medium Risk"
    elif performance == "Average":
        return "High Risk"
    else:
        return "Critical Risk"

risk = risk_level(prediction)

# ---------------------------
# OUTPUT

print("\n🎯 Performance:", prediction)
print("⚠️ Risk Level:", risk)

print("\n🚀 ANALYSIS COMPLETED\n")