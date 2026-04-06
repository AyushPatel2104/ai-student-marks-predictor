import pandas as pd
import os

# -------------------------------
# PATH SETUP
current_dir = os.path.dirname(__file__)
week4_dir = os.path.abspath(os.path.join(current_dir, ".."))

input_path = os.path.join(week4_dir, "datasets", "student_performance_final.csv")
output_path = os.path.join(week4_dir, "datasets", "student_performance_encoded.csv")

# -------------------------------
# LOAD DATA
data = pd.read_csv(input_path)

print("\nEncoding Started\n")

# -------------------------------
# 1. Encode Gender

data["Gender"] = data["Gender"].map({
    "Male": 1,
    "Female": 0
})

# -------------------------------
# 2. Encode Performance Category

data["Performance_Category"] = data["Performance_Category"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

# -------------------------------
# PREVIEW

print(data.head())

# -------------------------------
# SAVE DATA

data.to_csv(output_path, index=False)

print("\nEncoded dataset saved at:", output_path)
print("Encoding Completed ✅")