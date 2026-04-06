import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

current_dir = os.path.dirname(__file__)
week3_dir = os.path.abspath(os.path.join(current_dir, ".."))

dataset_path = os.path.join(week3_dir, "datasets", "student_performance_cleaned.csv")
output_folder = os.path.join(week3_dir, "outputs")

os.makedirs(output_folder, exist_ok=True)

data = pd.read_csv(dataset_path)

print("Week 3 Setup Done Successfully")

# -------------------------------
# GRAPH 1 — Study Hours vs Score

plt.figure()

sns.scatterplot(
    x=data["Study_Hours_per_Day"],
    y=data["Final_Exam_Score"]
)

plt.title("Study Hours vs Final Exam Score")

file1 = os.path.join(output_folder, "study_vs_score.png")
plt.savefig(file1)

plt.show()

# -------------------------------
# GRAPH 2 — Attendance vs Score

plt.figure()

sns.scatterplot(
    x=data["Attendance_Percentage"],
    y=data["Final_Exam_Score"]
)

plt.title("Attendance vs Final Exam Score")

file2 = os.path.join(output_folder, "attendance_vs_score.png")
plt.savefig(file2)

plt.show()

# -------------------------------
# GRAPH 3 — Gender vs Performance

plt.figure()

sns.boxplot(
    x=data["Gender"],
    y=data["Final_Exam_Score"]
)

plt.title("Gender vs Student Performance")

file3 = os.path.join(output_folder, "gender_performance.png")
plt.savefig(file3)

plt.show()

# -------------------------------
# GRAPH 4 — Score Distribution

plt.figure()

sns.histplot(
    data["Final_Exam_Score"],
    bins=30
)

plt.title("Final Exam Score Distribution")

file4 = os.path.join(output_folder, "score_distribution.png")
plt.savefig(file4)

plt.show()

# -------------------------------
# GRAPH 5 — Correlation Heatmap

plt.figure(figsize=(10,6))

corr = data.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Feature Correlation Heatmap")

file5 = os.path.join(output_folder, "correlation_heatmap.png")
plt.savefig(file5)

plt.show()