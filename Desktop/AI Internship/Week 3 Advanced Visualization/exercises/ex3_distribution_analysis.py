import pandas as pd
import os

current_dir = os.path.dirname(__file__)
week3_dir = os.path.abspath(os.path.join(current_dir, ".."))

file_path = os.path.join(week3_dir, "datasets", "student_performance_cleaned.csv")

data = pd.read_csv(file_path)

high_scores = len(data[data["Final_Exam_Score"] > 85])
mid_scores = len(data[(data["Final_Exam_Score"] >= 50) & (data["Final_Exam_Score"] <= 85)])
low_scores = len(data[data["Final_Exam_Score"] < 50])

print("High Scorers:", high_scores)
print("Average Scorers:", mid_scores)
print("Low Scorers:", low_scores)