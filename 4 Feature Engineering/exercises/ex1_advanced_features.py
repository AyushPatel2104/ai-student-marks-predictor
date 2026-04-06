import pandas as pd
import os

current_dir = os.path.dirname(__file__)
week4_dir = os.path.abspath(os.path.join(current_dir, ".."))

file_path = os.path.join(week4_dir, "datasets", "student_performance_encoded.csv")

data = pd.read_csv(file_path)

# New Advanced Features
data["Study_Attendance_Score"] = data["Study_Hours_per_Day"] * data["Attendance_Percentage"]
data["Score_per_Attendance"] = data["Final_Exam_Score"] / data["Attendance_Percentage"]

print(data.head())