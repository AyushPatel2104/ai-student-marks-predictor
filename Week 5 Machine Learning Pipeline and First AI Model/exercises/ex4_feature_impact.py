import joblib
import os
import pandas as pd

current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

model = joblib.load(os.path.join(week5_dir, "outputs", "student_model.pkl"))

print("\nImpact of Study Hours\n")

for h in range(1,10):
    sample = pd.DataFrame({
        "Study_Hours_per_Day":[h],
        "Attendance_Percentage":[80],
        "Previous_Exam_Score":[70]
    })

    pred = model.predict(sample)

    print(f"Study Hours: {h} → Score: {round(pred[0],2)}")