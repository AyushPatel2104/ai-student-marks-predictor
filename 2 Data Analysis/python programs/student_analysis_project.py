import pandas as pd
import matplotlib.pyplot as plt
import os

# Path setup
current_dir = os.path.dirname(__file__)
week2_dir = os.path.abspath(os.path.join(current_dir, ".."))

dataset_path = os.path.join(week2_dir, "datasets", "student_performance_cleaned.csv")
output_folder = os.path.join(week2_dir, "outputs")

os.makedirs(output_folder, exist_ok=True)

# Load dataset
data = pd.read_csv(dataset_path)

print("\n===================================")
print("   STUDENT PERFORMANCE ANALYSIS")
print("===================================\n")

# -------------------------------
# Basic Calculations

avg_score = round(data["Final_Exam_Score"].mean(), 2)

top_student = data.loc[data["Final_Exam_Score"].idxmax()]
low_student = data.loc[data["Final_Exam_Score"].idxmin()]

above_avg = len(data[data["Final_Exam_Score"] > avg_score])
below_avg = len(data[data["Final_Exam_Score"] < avg_score])

# -------------------------------
# SIMPLE OUTPUT (Human Friendly)

print(f"📊 Average Score of Students: {avg_score}")

print("\n🏆 Top Performing Student:")
print(f"Score: {round(top_student['Final_Exam_Score'],2)}")
print(f"Study Hours: {top_student['Study_Hours_per_Day']}")
print(f"Attendance: {top_student['Attendance_Percentage']}%")

print("\n⚠️ Lowest Performing Student:")
print(f"Score: {round(low_student['Final_Exam_Score'],2)}")
print(f"Study Hours: {low_student['Study_Hours_per_Day']}")
print(f"Attendance: {low_student['Attendance_Percentage']}%")

print("\n📈 Summary:")
print(f"Students Above Average: {above_avg}")
print(f"Students Below Average: {below_avg}")

# -------------------------------
# GRAPH 1 — Bar Chart

plt.figure()
labels = ["Above Avg", "Below Avg"]
values = [above_avg, below_avg]

plt.bar(labels, values)

plt.title("Students Above vs Below Average")

file1 = os.path.join(output_folder, "above_vs_below.png")
plt.savefig(file1)
plt.show()

print("\nSaved:", file1)

# -------------------------------
# GRAPH 2 — Pie Chart

plt.figure()
plt.pie(values, labels=labels, autopct="%1.1f%%")

plt.title("Performance Distribution")

file2 = os.path.join(output_folder, "performance_pie.png")
plt.savefig(file2)
plt.show()

print("Saved:", file2)