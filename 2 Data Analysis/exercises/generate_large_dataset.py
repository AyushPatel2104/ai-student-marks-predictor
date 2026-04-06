import pandas as pd
import numpy as np
import os

np.random.seed(42)

num_students = 1200

data = {
    "Student_ID": range(1, num_students + 1),
    "Gender": np.random.choice(["Male", "Female"], num_students),
    "Age": np.random.randint(17, 22, num_students),
    "Study_Hours_per_Day": np.random.randint(1, 10, num_students),
    "Sleep_Hours": np.random.randint(4, 9, num_students),
    "Attendance_Percentage": np.random.randint(60, 100, num_students),
    "Assignments_Completed": np.random.randint(0, 10, num_students),
    "Previous_Exam_Score": np.random.randint(40, 95, num_students),
    "Internet_Access": np.random.choice(["Yes", "No"], num_students),
    "Family_Income_Level": np.random.choice(["Low","Medium","High"], num_students)
}

df = pd.DataFrame(data)

df["Final_Exam_Score"] = (
    df["Study_Hours_per_Day"] * 5 +
    df["Attendance_Percentage"] * 0.3 +
    df["Previous_Exam_Score"] * 0.4 +
    np.random.randint(-10,10,num_students)
)

# get current script location
current_dir = os.path.dirname(__file__)

# move one level up to Week 2 folder
week2_dir = os.path.abspath(os.path.join(current_dir, ".."))

# datasets folder path
dataset_folder = os.path.join(week2_dir, "datasets")

# create folder if missing
os.makedirs(dataset_folder, exist_ok=True)

# file path
file_path = os.path.join(dataset_folder, "student_performance_large.csv")

df.to_csv(file_path, index=False)

print("Dataset generated successfully with", num_students, "rows")
print("File saved at:", file_path)