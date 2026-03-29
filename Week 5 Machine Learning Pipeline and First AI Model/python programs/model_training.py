import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# -------------------------------
# PATH SETUP
current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

dataset_path = os.path.join(week5_dir, "datasets", "student_performance_encoded.csv")
output_path = os.path.join(week5_dir, "outputs", "model_results.txt")

# -------------------------------
# LOAD DATA
data = pd.read_csv(dataset_path)


data = data.dropna()

print("\nMODEL TRAINING STARTED\n")

# -------------------------------
# -------------------------------
# SELECT ONLY REQUIRED NUMERIC FEATURES

features = [
    "Study_Hours_per_Day",
    "Attendance_Percentage",
    "Previous_Exam_Score"
]

X = data[features]
y = data["Final_Exam_Score"]
print(X.dtypes)
# -------------------------------
# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# MODEL

model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# PREDICTION

y_pred = model.predict(X_test)

# -------------------------------
# EVALUATION

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# -------------------------------
# OUTPUT

result = f"""
MODEL RESULTS

Mean Absolute Error (MAE): {round(mae,2)}
Mean Squared Error (MSE): {round(mse,2)}
"""

print(result)

# Save output
with open(output_path, "w") as f:
    f.write(result)

print("Results saved at:", output_path)

