from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# ---------------------------
# LOAD MODEL

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "models", "pipeline_model.pkl")

if not os.path.exists(model_path):
    print("❌ Model not found!")
    exit()

model = joblib.load(model_path)

# ---------------------------
# HOME ROUTE

@app.route("/")
def home():
    return render_template("index.html")

# ---------------------------
# PREDICTION API

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # CREATE INPUT
        input_df = pd.DataFrame([{
            "Student_ID": 0,
            "Age": float(data["age"]),
            "Study_Hours_per_Day": float(data["study_hours"]),
            "Sleep_Hours": float(data["sleep_hours"]),
            "Attendance_Percentage": float(data["attendance"]),
            "Assignments_Completed": float(data["assignments"]),
            "Previous_Exam_Score": float(data["previous_score"])
        }])

        # MODEL PREDICTION
        prediction = model.predict(input_df)[0]

        # ---------------------------
        # RISK

        if prediction == "Excellent":
            risk = "Low Risk"
        elif prediction == "Good":
            risk = "Medium Risk"
        elif prediction == "Average":
            risk = "High Risk"
        else:
            risk = "Critical Risk"

        # ---------------------------
        # SCORE

        score = (
            float(data["study_hours"]) * 10 +
            float(data["attendance"]) * 0.5 +
            float(data["previous_score"]) * 0.4
        ) / 2

        # ---------------------------
        # SUGGESTION + DESCRIPTION

        if prediction == "Excellent":
            suggestion = "Keep it up! You're doing great 🚀"
            description = "Top performer with strong consistency"
            tips = "Maintain your routine and aim for mastery"
        elif prediction == "Good":
            suggestion = "Improve consistency to reach excellence 💪"
            description = "Above average performance"
            tips = "Focus on weak areas and improve consistency"
        elif prediction == "Average":
            suggestion = "Focus more on studies and attendance 📚"
            description = "Moderate performance"
            tips = "Increase study time and reduce distractions"
        else:
            suggestion = "Immediate improvement required ⚠️"
            description = "At risk student"
            tips = "Follow strict study schedule and seek help"

        # ---------------------------
        # LOGGING

        log_path = os.path.join(BASE_DIR, "outputs", "api_logs.txt")
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        with open(log_path, "a") as f:
            f.write(f"{datetime.now()} | Input: {data} | Output: {prediction}, {risk}, {score}\n")

        # ---------------------------
        # RESPONSE

        return jsonify({
            "performance": str(prediction),
            "risk_level": str(risk),
            "predicted_score": round(score, 2),
            "suggestion": suggestion,
            "description": description,
            "tips": tips
        })

    except Exception as e:
        return jsonify({"error": str(e)})

# ---------------------------

if __name__ == "__main__":
    app.run(debug=True)