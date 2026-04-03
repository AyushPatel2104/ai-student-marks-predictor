import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("\n🔹 WEEK 7 — EDA STARTED 🔹\n")

# ---------------------------
# LOAD CLEAN DATASET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "..", "outputs", "clean_classification_data.csv")

if not os.path.exists(file_path):
    print("❌ Clean dataset not found! Run preprocessing first.")
    exit()

df = pd.read_csv(file_path)

print("✅ Dataset Loaded")
print("Shape:", df.shape)

# ---------------------------
# CREATE GRAPH FOLDER

graph_dir = os.path.join(BASE_DIR, "..", "outputs", "graphs")
os.makedirs(graph_dir, exist_ok=True)

# ---------------------------
# 1. CLASS DISTRIBUTION

plt.figure()
sns.countplot(x="Performance", data=df)
plt.title("Student Performance Distribution")

path1 = os.path.join(graph_dir, "class_distribution.png")
plt.savefig(path1)
plt.close()

print("✅ Class distribution graph saved")

# ---------------------------
# 2. NUMERIC DISTRIBUTION

numeric_cols = df.select_dtypes(include=['number']).columns

for col in numeric_cols:
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")

    path = os.path.join(graph_dir, f"{col}_distribution.png")
    plt.savefig(path)
    plt.close()

print("✅ Numeric distribution graphs saved")

# ---------------------------
# 3. CORRELATION HEATMAP

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")

path2 = os.path.join(graph_dir, "correlation_heatmap.png")
plt.savefig(path2)
plt.close()

print("✅ Correlation heatmap saved")

# ---------------------------
# 4. BOXPLOT (OUTLIERS)

for col in numeric_cols:
    plt.figure()
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")

    path = os.path.join(graph_dir, f"{col}_boxplot.png")
    plt.savefig(path)
    plt.close()

print("✅ Boxplots saved")

print("\n🚀 EDA COMPLETED\n")