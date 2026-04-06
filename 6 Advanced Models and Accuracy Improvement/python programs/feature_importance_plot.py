import joblib
import matplotlib.pyplot as plt
import os

current_dir = os.path.dirname(__file__)
week6_dir = os.path.abspath(os.path.join(current_dir, ".."))

model_path = os.path.join(week6_dir, "outputs", "final_model.pkl")

model = joblib.load(model_path)

features = ["Study_Hours_per_Day", "Attendance_Percentage", "Previous_Exam_Score"]
importance = model.feature_importances_

plt.figure()
plt.bar(features, importance)

plt.title("Feature Importance (Random Forest)")
plt.xlabel("Features")
plt.ylabel("Importance")

plt.savefig(os.path.join(week6_dir, "outputs", "feature_importance.png"))

plt.show()