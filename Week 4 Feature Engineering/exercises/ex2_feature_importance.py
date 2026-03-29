import pandas as pd
import os

current_dir = os.path.dirname(__file__)
week4_dir = os.path.abspath(os.path.join(current_dir, ".."))

file_path = os.path.join(week4_dir, "datasets", "student_performance_encoded.csv")

data = pd.read_csv(file_path)

corr = data.corr(numeric_only=True)

print("\nFeature Importance (Correlation with Final Score):\n")
print(corr["Final_Exam_Score"].sort_values(ascending=False))