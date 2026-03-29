import pandas as pd
import os
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# -------------------------------
# PATH
current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

data_path = os.path.join(week5_dir, "datasets", "student_performance_encoded.csv")
output_path = os.path.join(week5_dir, "outputs", "model_comparison.png")

# -------------------------------
# LOAD DATA
data = pd.read_csv(data_path)

# -------------------------------
# FEATURES

features = [
    "Study_Hours_per_Day",
    "Attendance_Percentage",
    "Previous_Exam_Score"
]

X = data[features]
y = data["Final_Exam_Score"]

# -------------------------------
# SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# MODELS

lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_mae = mean_absolute_error(y_test, lr_pred)

dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)
dt_mae = mean_absolute_error(y_test, dt_pred)

# -------------------------------
# PLOT

models = ["Linear Regression", "Decision Tree"]
errors = [lr_mae, dt_mae]

plt.bar(models, errors)

plt.title("Model Comparison (MAE)")
plt.xlabel("Models")
plt.ylabel("Error")

# SAVE
plt.savefig(output_path)

plt.show()

print("Comparison plot saved at:", output_path)