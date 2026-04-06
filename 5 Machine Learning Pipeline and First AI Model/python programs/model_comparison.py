import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# -------------------------------
# PATH
current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

data_path = os.path.join(week5_dir, "datasets", "student_performance_encoded.csv")

# -------------------------------
# LOAD DATA
data = pd.read_csv(data_path)

# -------------------------------
# FEATURES (NO DATA LEAKAGE)

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
# LINEAR REGRESSION

lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

lr_mae = mean_absolute_error(y_test, lr_pred)

# -------------------------------
# DECISION TREE

dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)

dt_mae = mean_absolute_error(y_test, dt_pred)

# -------------------------------
# RESULTS

print("\nMODEL COMPARISON\n")

print("Linear Regression MAE:", round(lr_mae, 2))
print("Decision Tree MAE:", round(dt_mae, 2))

# -------------------------------
# BEST MODEL

if lr_mae < dt_mae:
    print("\nBest Model: Linear Regression")
else:
    print("\nBest Model: Decision Tree")
    
    