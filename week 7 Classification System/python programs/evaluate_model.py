import pandas as pd
import os
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

print("\n🔹 WEEK 7 — MODEL EVALUATION STARTED 🔹\n")

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
# FEATURES & TARGET

X = df.drop(columns=["Performance", "Final_Exam_Score"])
y = df["Performance"]

X = X.select_dtypes(include=['number'])

# ---------------------------
# SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------
# PREDICTIONS

y_pred = model.predict(X_test)

# ---------------------------
# CONFUSION MATRIX

cm = confusion_matrix(y_test, y_pred)

print("\n📊 Confusion Matrix:\n", cm)

# ---------------------------
# SAVE GRAPH

graph_dir = os.path.join(BASE_DIR, "..", "outputs", "graphs")
os.makedirs(graph_dir, exist_ok=True)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues")

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

graph_path = os.path.join(graph_dir, "confusion_matrix.png")
plt.savefig(graph_path)
plt.close()

print("✅ Confusion matrix graph saved")

# ---------------------------
# ERROR ANALYSIS

results = X_test.copy()
results["Actual"] = y_test.values
results["Predicted"] = y_pred

errors = results[results["Actual"] != results["Predicted"]]

print(f"\n❌ Total Wrong Predictions: {len(errors)}")

# Save errors
error_path = os.path.join(BASE_DIR, "..", "outputs", "error_analysis.csv")
errors.to_csv(error_path, index=False)

print("✅ Error analysis file saved")

print("\n🚀 MODEL EVALUATION COMPLETED\n")