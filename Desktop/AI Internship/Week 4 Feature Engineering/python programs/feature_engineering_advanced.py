import pandas as pd
import os

# -------------------------------
# PATH SETUP
current_dir = os.path.dirname(__file__)
week4_dir = os.path.abspath(os.path.join(current_dir, ".."))

dataset_path = os.path.join(week4_dir, "datasets", "student_performance_cleaned.csv")
output_path = os.path.join(week4_dir, "datasets", "student_performance_final.csv")

# -------------------------------
# LOAD DATA
data = pd.read_csv(dataset_path)

print("\nFeature Engineering Started\n")

# -------------------------------
# 1. Study Efficiency

data["Study_Efficiency"] = data["Final_Exam_Score"] / data["Study_Hours_per_Day"]

# -------------------------------
# 2. Score Improvement

data["Score_Improvement"] = data["Final_Exam_Score"] - data["Previous_Exam_Score"]

# -------------------------------
# 3. Performance Category

def performance(score):
    if score >= 85:
        return "High"
    elif score >= 60:
        return "Medium"
    else:
        return "Low"

data["Performance_Category"] = data["Final_Exam_Score"].apply(performance)

# -------------------------------
# PREVIEW

print(data.head())

# -------------------------------
# SAVE FINAL DATASET

data.to_csv(output_path, index=False)

print("\nFinal dataset saved at:", output_path)
print("Feature Engineering Completed ✅")