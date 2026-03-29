import joblib
import os
import pandas as pd

current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

model = joblib.load(os.path.join(week5_dir, "outputs", "student_model.pkl"))

print("\nTest Different Inputs\n")

for i in range(3):
    try:
        study = float(input("Study Hours: ") or 0)
        att = float(input("Attendance: ") or 0)
        prev = float(input("Previous Score: ") or 0)

        sample = pd.DataFrame({
            "Study_Hours_per_Day":[study],
            "Attendance_Percentage":[att],
            "Previous_Exam_Score":[prev]
        })

        pred = model.predict(sample)

        print("Predicted Score:", round(pred[0],2))
        print("--------------------")

    except Exception as e:
        print("Invalid input! Please enter numbers only.\n")