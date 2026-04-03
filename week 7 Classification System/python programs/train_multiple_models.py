import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import joblib

print("\n🔹 WEEK 7 — MODEL TRAINING STARTED 🔹\n")

# ---------------------------
# LOAD DATA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "..", "outputs", "clean_classification_data.csv")

df = pd.read_csv(file_path)

print("✅ Dataset Loaded")
print("Shape:", df.shape)

# ---------------------------
# FEATURES & TARGET

X = df.drop(columns=["Performance", "Final_Exam_Score"])
y = df["Performance"]

# Keep only numeric features
X = X.select_dtypes(include=['number'])

print("\n📊 Features Used:", list(X.columns))

# ---------------------------
# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("✅ Data Split Completed")

# ---------------------------
# MODELS

models = {
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Logistic Regression": LogisticRegression(max_iter=1000)
}

results = {}

# ---------------------------
# TRAIN & EVALUATE

for name, model in models.items():
    print(f"\n🚀 Training {name}...")

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)
    results[name] = acc

    print(f"✅ {name} Accuracy: {acc:.4f}")
    print("Classification Report:\n", classification_report(y_test, predictions))

# ---------------------------
# BEST MODEL

best_model_name = max(results, key=results.get)
best_model = models[best_model_name]

print(f"\n🏆 Best Model: {best_model_name}")

# ---------------------------
# SAVE MODEL

model_dir = os.path.join(BASE_DIR, "..", "outputs", "models")
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, "best_model.pkl")

joblib.dump(best_model, model_path)

print(f"💾 Model saved at: {model_path}")

print("\n🚀 MODEL TRAINING COMPLETED\n")