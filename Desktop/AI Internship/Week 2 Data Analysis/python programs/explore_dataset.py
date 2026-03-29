import pandas as pd
import os
from tabulate import tabulate

# Ensure outputs folder exists
os.makedirs("../outputs", exist_ok=True)

# Path for report file
report_path = "../outputs/week2_dataset_report.txt"
report = open(report_path, "w", encoding="utf-8")

# Function to print and save report text
def write(text=""):
    print(text)
    report.write(text + "\n")

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:.2f}'.format

# Load dataset
data = pd.read_csv("../datasets/student_performance_large.csv")

write("="*70)
write("STUDENT PERFORMANCE DATASET EXPLORATION REPORT")
write("="*70)

# -------------------------------------------------
write("\n[1] FIRST 10 ROWS OF DATASET\n")
table1 = tabulate(data.head(10), headers='keys', tablefmt='grid')
write(table1)

# -------------------------------------------------
rows, cols = data.shape

write("\n[2] DATASET SIZE\n")

size_table = [
    ["Total Rows", rows],
    ["Total Columns", cols]
]

table2 = tabulate(size_table, headers=["Metric","Value"], tablefmt="grid")
write(table2)

# -------------------------------------------------
write("\n[3] COLUMN NAMES\n")

column_table = [[i+1, col] for i, col in enumerate(data.columns)]
table3 = tabulate(column_table, headers=["Index","Column Name"], tablefmt="grid")
write(table3)

# -------------------------------------------------
write("\n[4] DATASET INFORMATION\n")

info_table = []
for col in data.columns:
    info_table.append([
        col,
        str(data[col].dtype),
        data[col].count()
    ])

table4 = tabulate(info_table,
               headers=["Column","Data Type","Non-Null Count"],
               tablefmt="grid")

write(table4)

# -------------------------------------------------
write("\n[5] STATISTICAL SUMMARY (EASY TO UNDERSTAND)\n")

summary = data.describe()

summary.rename(index={
    "count": "Total Records",
    "mean": "Average Value",
    "std": "Variation (Std Dev)",
    "min": "Minimum Value",
    "25%": "25% Students Below",
    "50%": "Median Value",
    "75%": "75% Students Below",
    "max": "Maximum Value"
}, inplace=True)

write(summary.to_string())

# -------------------------------------------------
write("\n" + "="*70)
write("END OF DATASET REPORT")
write("="*70)

# Close report file
report.close()

print("\nReport saved at:", report_path)