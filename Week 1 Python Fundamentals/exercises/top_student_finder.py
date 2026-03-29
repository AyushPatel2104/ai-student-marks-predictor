import pandas as pd

data = pd.read_csv("C:/Users/Ayush patel/Desktop/AI Internship/Week 1 Python Fundamentals/datasets/student_data.csv")

data["Total"] = data["Maths"] + data["Science"] + data["English"]

top_student = data.loc[data["Total"].idxmax()]

print("Top Student:")

print(top_student)