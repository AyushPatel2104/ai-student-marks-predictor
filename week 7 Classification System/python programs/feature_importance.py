import pandas as pd
import os
import joblib
import matplotlib.pyplot as plt

print("\n🔹 WEEK 7 — FEATURE IMPORTANCE STARTED 🔹\n")

# ---------------------------
# LOAD DATA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "outputs", "clean_classification_data.csv")

df = pd.read_csv(data_path)

# ---------------------------
# LOAD MODEL

model_path = os.path.join(BASE_DIR, "..", "outputs", "models", "best_model.pkl")
model = joblib.load(model_path)

print("✅ Model Loaded")

# ---------------------------
# FEATURES

X = df.drop(columns=["Performance", "Final_Exam_Score"])
X = X.select_dtypes(include=['number'])

feature_names = X.columns

# ---------------------------
# CHECK IF MODEL SUPPORTS IMPORTANCE

if hasattr(model, "feature_importances_"):
    importance = model.feature_importances_
else:
    print("❌ This model does not support feature importance")
    exit()

# ---------------------------
# CREATE DATAFRAME

feature_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

feature_df = feature_df.sort_values(by="Importance", ascending=False)

print("\n📊 Feature Importance:\n")
print(feature_df)

# ---------------------------
# SAVE GRAPH

graph_dir = os.path.join(BASE_DIR, "..", "outputs", "graphs")
os.makedirs(graph_dir, exist_ok=True)

plt.figure(figsize=(8,5))
plt.barh(feature_df["Feature"], feature_df["Importance"])
plt.title("Feature Importance")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.gca().invert_yaxis()

graph_path = os.path.join(graph_dir, "feature_importance.png")
plt.savefig(graph_path)
plt.close()

print("✅ Feature importance graph saved")

# ---------------------------
# SAVE CSV

csv_path = os.path.join(BASE_DIR, "..", "outputs", "feature_importance.csv")
feature_df.to_csv(csv_path, index=False)

print("✅ Feature importance file saved")

print("\n🚀 FEATURE IMPORTANCE COMPLETED\n")