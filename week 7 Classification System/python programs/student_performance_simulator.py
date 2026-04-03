import joblib
import os
import pandas as pd

print("\n🔹 STUDENT PERFORMANCE SIMULATOR 🔹\n")

# ---------------------------
# LOAD MODEL

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "..", "outputs", "models", "pipeline_model.pkl")

if not os.path.exists(model_path):
    print("❌ Model not found! Run pipeline_model.py first.")
    exit()

model = joblib.load(model_path)

print("✅ Model Loaded")

# ---------------------------
# SCENARIOS

scenarios = [
    {
        "name": "Low Study + Low Attendance",
        "data": [0, 18, 2, 6, 50, 2, 40]
    },
    {
        "name": "High Study + High Attendance",
        "data": [0, 20, 9, 7, 95, 10, 85]
    },
    {
        "name": "High Study + Low Attendance",
        "data": [0, 19, 9, 6, 55, 5, 70]
    },
    {
        "name": "Low Study + High Attendance",
        "data": [0, 21, 3, 7, 90, 6, 60]
    },
    {
        "name": "Average Student",
        "data": [0, 20, 5, 7, 75, 5, 65]
    }
]

# ---------------------------
# FEATURE NAMES

columns = [
    "Student_ID",
    "Age",
    "Study_Hours_per_Day",
    "Sleep_Hours",
    "Attendance_Percentage",
    "Assignments_Completed",
    "Previous_Exam_Score"
]

# ---------------------------
# RISK FUNCTION

def risk(perf):
    if perf == "Excellent":
        return "Low Risk"
    elif perf == "Good":
        return "Medium Risk"
    elif perf == "Average":
        return "High Risk"
    else:
        return "Critical Risk"

# ---------------------------
# RUN SIMULATION

print("\n📊 Running Scenarios...\n")

for scenario in scenarios:
    input_df = pd.DataFrame([scenario["data"]], columns=columns)

    prediction = model.predict(input_df)[0]
    risk_level = risk(prediction)

    print(f"🔹 Scenario: {scenario['name']}")
    print(f"   ➤ Predicted Performance: {prediction}")
    print(f"   ⚠️ Risk Level: {risk_level}\n")

print("🚀 SIMULATION COMPLETED\n")