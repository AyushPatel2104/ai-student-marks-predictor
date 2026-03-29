import pandas as pd
import os

# Get current script directory
current_dir = os.path.dirname(__file__)

# Move one level up (Week 2 Data Analysis)
week2_dir = os.path.abspath(os.path.join(current_dir, ".."))

# Define dataset path
dataset_path = os.path.join(week2_dir, "datasets", "student_performance_large.csv")

# Define outputs folder
outputs_folder = os.path.join(week2_dir, "outputs")

# Create outputs folder if it doesn't exist
os.makedirs(outputs_folder, exist_ok=True)

# Define report file
report_path = os.path.join(outputs_folder, "missing_value_report.txt")

# Load dataset
data = pd.read_csv(dataset_path)

print("\n===============================")
print("MISSING VALUE ANALYSIS REPORT")
print("===============================\n")

missing_values = data.isnull().sum()

# Write report
with open(report_path, "w") as report:

    report.write("MISSING VALUE ANALYSIS REPORT\n\n")

    for column in missing_values.index:
        line = f"{column} : {missing_values[column]}"
        print(line)
        report.write(line + "\n")

    total_missing = missing_values.sum()

    print("\nTotal Missing Values:", total_missing)
    report.write("\nTotal Missing Values: " + str(total_missing))

print("\nReport saved at:")
print(report_path)