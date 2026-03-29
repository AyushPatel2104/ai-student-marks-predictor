import joblib
import os

# -------------------------------
# PATH SETUP
current_dir = os.path.dirname(__file__)
week5_dir = os.path.abspath(os.path.join(current_dir, ".."))

model_path = os.path.join(week5_dir, "outputs", "student_model.pkl")

# -------------------------------
# LOAD MODEL
model = joblib.load(model_path)

print("✅ Model Loaded Successfully\n")

# -------------------------------
# MODEL TYPE
print("Model Type:")
print(type(model))

# -------------------------------
# COEFFICIENTS
print("\nModel Coefficients:")
print(model.coef_)

# -------------------------------
# INTERCEPT
print("\nIntercept:")
print(model.intercept_)