import joblib
import os
import pandas as pd

current_dir = os.path.dirname(__file__)
week6_dir = os.path.abspath(os.path.join(current_dir, ".."))

model_path = os.path.join(week6_dir, "outputs", "final_model.pkl")

model = joblib.load(model_path)

# SAMPLE INPUT
sample = pd.DataFrame({
    "Study_Hours_per_Day":[6],
    "Attendance_Percentage":[85],
    "Previous_Exam_Score":[75]
})

pred = model.predict(sample)

print("Final Model Prediction:", round(pred[0],2))