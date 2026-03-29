import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# PATH SETUP
current_dir = os.path.dirname(__file__)
week2_dir = os.path.abspath(os.path.join(current_dir, ".."))

dataset_path = os.path.join(week2_dir, "datasets", "student_performance_cleaned.csv")
output_folder = os.path.join(week2_dir, "outputs")

os.makedirs(output_folder, exist_ok=True)

# -------------------------------
# LOAD DATA
data = pd.read_csv(dataset_path)

print("\n===============================")
print(" FULL DATA ANALYSIS SYSTEM ")
print("===============================\n")

# -------------------------------
# DATA CLEANING

data = data.drop_duplicates()

# -------------------------------
# FEATURE ENGINEERING

data["Total_Score"] = data["Previous_Exam_Score"] + data["Final_Exam_Score"]
data["Study_Efficiency"] = data["Final_Exam_Score"] / data["Study_Hours_per_Day"]

# -------------------------------
# ANALYSIS

avg_score = round(data["Final_Exam_Score"].mean(), 2)

top_student = data.loc[data["Final_Exam_Score"].idxmax()]
low_student = data.loc[data["Final_Exam_Score"].idxmin()]

above_avg = len(data[data["Final_Exam_Score"] > avg_score])
below_avg = len(data[data["Final_Exam_Score"] < avg_score])

# -------------------------------
# PRINT OUTPUT

print(f"📊 Average Score: {avg_score}")

print("\n🏆 Top Student:")
print(f"Score: {round(top_student['Final_Exam_Score'],2)}")
print(f"Study Hours: {top_student['Study_Hours_per_Day']}")
print(f"Attendance: {top_student['Attendance_Percentage']}%")

print("\n⚠️ Lowest Student:")
print(f"Score: {round(low_student['Final_Exam_Score'],2)}")
print(f"Study Hours: {low_student['Study_Hours_per_Day']}")
print(f"Attendance: {low_student['Attendance_Percentage']}%")

print("\n📈 Summary:")
print(f"Above Avg Students: {above_avg}")
print(f"Below Avg Students: {below_avg}")

# -------------------------------
# GRAPH 1 — BAR

plt.figure()
plt.bar(["Above Avg", "Below Avg"], [above_avg, below_avg])
plt.title("Performance Distribution")

file1 = os.path.join(output_folder, "final_bar_chart.png")
plt.savefig(file1)
plt.show()

# -------------------------------
# GRAPH 2 — PIE

plt.figure()
plt.pie([above_avg, below_avg], labels=["Above", "Below"], autopct="%1.1f%%")
plt.title("Student Performance Split")

file2 = os.path.join(output_folder, "final_pie_chart.png")
plt.savefig(file2)
plt.show()

# -------------------------------
# SAVE REPORT

report_path = os.path.join(output_folder, "final_analysis_report.txt")

report = f"""
FULL DATA ANALYSIS REPORT

Average Score: {avg_score}

Top Student Score: {top_student['Final_Exam_Score']}
Lowest Student Score: {low_student['Final_Exam_Score']}

Students Above Avg: {above_avg}
Students Below Avg: {below_avg}
"""

with open(report_path, "w") as f:
    f.write(report)

print("\n✅ Full Analysis Completed")
print("Report saved at:", report_path)