import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

data = pd.read_csv(os.path.join(week5_dir, "datasets", "student_performance_encoded.csv"))

features = [
    "Study_Hours_per_Day",
    "Attendance_Percentage",
    "Previous_Exam_Score"
]

X = data[features]
y = data["Final_Exam_Score"]

model = LinearRegression()
model.fit(X, y)

importance = model.coef_

plt.bar(features, importance)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Impact on Score")

output_path = os.path.join(week5_dir, "outputs", "feature_importance.png")
plt.savefig(output_path)

plt.show()

print("Plot saved at:", output_path)

plt.show()