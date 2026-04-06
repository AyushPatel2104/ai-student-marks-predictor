import pandas as pd

data = pd.read_csv("C:/Users/Ayush patel/Desktop/AI Internship/Week 1 Python Fundamentals/datasets/student_data.csv")

print("Dataset:")
print(data)

print("\nAverage Marks")

print(data.mean(numeric_only=True))