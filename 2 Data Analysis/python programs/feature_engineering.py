import pandas as pd
import os

# Path setup
current_dir = os.path.dirname(__file__)
week2_dir = os.path.abspath(os.path.join(current_dir, ".."))

file_path = os.path.join(week2_dir, "datasets", "student_performance_cleaned.csv")

# Load dataset
data = pd.read_csv(file_path)

print("Before Feature Engineering:\n")
print(data.head())

# --------------------------------------------------
# Feature 1: Total Score
data["Total_Score"] = data["Previous_Exam_Score"] + data["Final_Exam_Score"]

# Feature 2: Study Efficiency
data["Study_Efficiency"] = data["Final_Exam_Score"] / data["Study_Hours_per_Day"]

# --------------------------------------------------

print("\nAfter Feature Engineering:\n")
print(data.head())

# Save new dataset
new_file = os.path.join(week2_dir, "datasets", "student_performance_featured.csv")
data.to_csv(new_file, index=False)

print("\n✅ Feature Engineering Completed")
print("New dataset saved at:", new_file)