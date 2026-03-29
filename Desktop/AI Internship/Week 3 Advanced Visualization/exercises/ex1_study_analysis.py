import pandas as pd
import os

current_dir = os.path.dirname(__file__)
week3_dir = os.path.abspath(os.path.join(current_dir, ".."))

file_path = os.path.join(week3_dir, "datasets", "student_performance_cleaned.csv")

data = pd.read_csv(file_path)

high_study = data[data["Study_Hours_per_Day"] >= 7]
low_study = data[data["Study_Hours_per_Day"] <= 3]

print("Average score (High Study):", round(high_study["Final_Exam_Score"].mean(),2))
print("Average score (Low Study):", round(low_study["Final_Exam_Score"].mean(),2))