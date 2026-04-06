import joblib
import os
import pandas as pd

current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

model = joblib.load(os.path.join(week5_dir, "outputs", "student_model.pkl"))

test_cases = [
    [2, 60, 50],
    [6, 85, 70],
    [8, 90, 80]
]

for case in test_cases:
    sample = pd.DataFrame({
        "Study_Hours_per_Day": [case[0]],
        "Attendance_Percentage": [case[1]],
        "Previous_Exam_Score": [case[2]]
    })
    
    pred = model.predict(sample)
    
    print(f"Input: {case} → Predicted Score: {round(pred[0],2)}")