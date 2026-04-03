import pandas as pd
import os

print("\n🔹 WEEK 7 — DATA PREPROCESSING (FINAL VERSION) 🔹\n")

# ---------------------------
# LOAD DATASET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "..", "datasets", "student_performance_cleaned.csv")

print("Checking path:", file_path)

if not os.path.exists(file_path):
    print("❌ Dataset not found! Check path.")
    exit()

df = pd.read_csv(file_path)

print("✅ Dataset Loaded Successfully")
print("Shape:", df.shape)

# ---------------------------
# SHOW COLUMNS

print("\n📊 Columns in dataset:")
print(list(df.columns))

# ---------------------------
# HANDLE MISSING VALUES

print("\n🔍 Missing Values Check:")
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

print("✅ Missing values handled")

# ---------------------------
# AUTO DETECT TARGET COLUMN (SMART LOGIC)

possible_targets = ["final_score", "exam_score", "score", "marks", "result"]

target_column = None

for col in possible_targets:
    if col in df.columns:
        target_column = col
        break

# If not found → take last numeric column
if target_column is None:
    numeric_cols = df.select_dtypes(include=['number']).columns
    target_column = numeric_cols[-1]

print(f"\n🎯 Using '{target_column}' as target column")

# ---------------------------
# SCORE SUMMARY

print("\n📊 Score Summary:")
print(df[target_column].describe())

# ---------------------------
# CREATE CLASSIFICATION TARGET

def categorize(score):
    if score < 50:
        return "Fail"
    elif score < 65:
        return "Average"
    elif score < 80:
        return "Good"
    else:
        return "Excellent"

df["Performance"] = df[target_column].apply(categorize)

print("\n✅ Classification column created")

# ---------------------------
# CLASS DISTRIBUTION

print("\n📊 Class Distribution:")
print(df["Performance"].value_counts())

# ---------------------------
# SAVE CLEAN DATASET

output_dir = os.path.join(BASE_DIR, "..", "outputs")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "clean_classification_data.csv")

print("\n💾 Saving file at:", output_path)

df.to_csv(output_path, index=False)

print("✅ Clean dataset saved successfully")

print("\n🚀 DATA PREPROCESSING COMPLETED\n")