import pandas as pd
import os
from sklearn.metrics import mean_absolute_error

current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

data = pd.read_csv(os.path.join(week5_dir, "datasets", "student_performance_encoded.csv"))

X = data[["Study_Hours_per_Day","Attendance_Percentage","Previous_Exam_Score"]]
y = data["Final_Exam_Score"]

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,y)

pred = model.predict(X)

print("MAE:", mean_absolute_error(y, pred))