import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# PATH
current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

data_path = os.path.join(week5_dir, "datasets", "student_performance_encoded.csv")
output_path = os.path.join(week5_dir, "outputs", "linear_regression_plot.png")

# LOAD DATA
data = pd.read_csv(data_path)

# SINGLE FEATURE (for plotting)
X = data[["Study_Hours_per_Day"]]
y = data["Final_Exam_Score"]

# MODEL
model = LinearRegression()
model.fit(X, y)

# PREDICTION LINE
y_pred = model.predict(X)

# PLOT
plt.scatter(X, y)
plt.plot(X, y_pred)

plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")

# SAVE IMAGE
plt.savefig(output_path)

plt.show()

print("Plot saved at:", output_path)