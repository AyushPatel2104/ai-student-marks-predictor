import joblib
import os
import pandas as pd

# PATH FIX
current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

model_path = os.path.join(week5_dir, "outputs", "student_model.pkl")

# LOAD MODEL
model = joblib.load(model_path)

cases = [
    {"name":"Weak Student","study":2,"att":60,"prev":50},
    {"name":"Average Student","study":5,"att":75,"prev":65},
    {"name":"Top Student","study":8,"att":90,"prev":85}
]

for c in cases:
    sample = pd.DataFrame({
        "Study_Hours_per_Day":[c["study"]],
        "Attendance_Percentage":[c["att"]],
        "Previous_Exam_Score":[c["prev"]]
    })

    pred = model.predict(sample)

    print(f"{c['name']} → {round(pred[0],2)}")