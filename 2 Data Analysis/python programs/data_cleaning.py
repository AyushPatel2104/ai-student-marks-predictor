import pandas as pd
import os

# Get script directory
current_dir = os.path.dirname(__file__)

# Week 2 directory
week2_dir = os.path.abspath(os.path.join(current_dir, ".."))

# Dataset path
dataset_path = os.path.join(week2_dir, "datasets", "student_performance_large.csv")

# Output dataset path
clean_dataset_path = os.path.join(week2_dir, "datasets", "student_performance_cleaned.csv")

# Load dataset
data = pd.read_csv(dataset_path)

print("\n===============================")
print("DATA CLEANING REPORT")
print("===============================\n")

# ------------------------------------------------
# 1. Check duplicates
duplicate_rows = data.duplicated().sum()

print("Duplicate Rows Found:", duplicate_rows)

data["Final_Exam_Score"] = data["Final_Exam_Score"].round(2)

# Remove duplicates
data = data.drop_duplicates()

# ------------------------------------------------
# 2. Check invalid values

print("\nChecking invalid values...\n")

print("Age below 15:", (data["Age"] < 15).sum())
print("Age above 30:", (data["Age"] > 30).sum())

print("Study hours above 15:", (data["Study_Hours_per_Day"] > 15).sum())

print("Attendance above 100:", (data["Attendance_Percentage"] > 100).sum())

# ------------------------------------------------
# 3. Data types

print("\nData Types:\n")

print(data.dtypes)

# ------------------------------------------------
# Save cleaned dataset

data.to_csv(clean_dataset_path, index=False)

print("\nClean dataset saved at:")
print(clean_dataset_path)