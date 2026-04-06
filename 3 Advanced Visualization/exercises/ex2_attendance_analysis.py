import pandas as pd
import os

current_dir = os.path.dirname(__file__)
week3_dir = os.path.abspath(os.path.join(current_dir, ".."))

file_path = os.path.join(week3_dir, "datasets", "student_performance_cleaned.csv")

data = pd.read_csv(file_path)

high_att = data[data["Attendance_Percentage"] >= 85]
low_att = data[data["Attendance_Percentage"] <= 65]

print("High Attendance Avg Score:", round(high_att["Final_Exam_Score"].mean(),2))
print("Low Attendance Avg Score:", round(low_att["Final_Exam_Score"].mean(),2))