import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

print("\n🔹 WEEK 7 — PIPELINE MODEL STARTED 🔹\n")

# ---------------------------
# LOAD DATA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "..", "outputs", "clean_classification_data.csv")

df = pd.read_csv(file_path)

print("✅ Dataset Loaded")

# ---------------------------
# FEATURES & TARGET

X = df.drop(columns=["Performance", "Final_Exam_Score"])
y = df["Performance"]

X = X.select_dtypes(include=['number'])

print("📊 Features:", list(X.columns))

# ---------------------------
# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------
# CREATE PIPELINE

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier())
])

print("✅ Pipeline Created")

# ---------------------------
# TRAIN PIPELINE

pipeline.fit(X_train, y_train)

print("🚀 Pipeline Model Trained")

# ---------------------------
# SAVE PIPELINE

model_dir = os.path.join(BASE_DIR, "..", "outputs", "models")
os.makedirs(model_dir, exist_ok=True)

pipeline_path = os.path.join(model_dir, "pipeline_model.pkl")

joblib.dump(pipeline, pipeline_path)

print(f"💾 Pipeline saved at: {pipeline_path}")

print("\n🚀 PIPELINE COMPLETED\n")