import joblib
import os
import pandas as pd   # 👈 ADD THIS

# PATH
current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

model_path = os.path.join(week5_dir, "outputs", "student_model.pkl")

# LOAD MODEL
model = joblib.load(model_path)

# NEW INPUT (UPDATED)
sample = pd.DataFrame({
    "Study_Hours_per_Day": [5],
    "Attendance_Percentage": [80],
    "Previous_Exam_Score": [70]
})

prediction = model.predict(sample)

print("Predicted Final Score:", round(prediction[0], 2))