import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

current_dir = os.path.dirname(__file__)
week6_dir = os.path.abspath(os.path.join(current_dir, ".."))

data_path = os.path.join(week6_dir, "datasets", "student_performance_encoded.csv")
model_path = os.path.join(week6_dir, "outputs", "final_model.pkl")

data = pd.read_csv(data_path)

features = ["Study_Hours_per_Day", "Attendance_Percentage", "Previous_Exam_Score"]

X = data[features]
y = data["Final_Exam_Score"]

model = joblib.load(model_path)

predictions = model.predict(X)

plt.figure()
plt.scatter(y, predictions)

plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.title("Actual vs Predicted")

plt.savefig(os.path.join(week6_dir, "outputs", "actual_vs_predicted.png"))

plt.show()