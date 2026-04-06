from flask import Flask, render_template_string, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

# -------------------------------
# LOAD MODEL (SAFE)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "outputs", "final_model.pkl")

model = None

try:
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print("✅ Model loaded successfully")
    else:
        print("❌ Model file not found")
except Exception as e:
    print("❌ Error loading model:", e)
    model = None

# -------------------------------
# HTML UI

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Student Predictor</title>

    <style>
        body {
            font-family: Arial;
            background: linear-gradient(to right, #667eea, #764ba2);
            text-align: center;
            color: white;
            padding-top: 50px;
        }

        .container {
            background: white;
            color: black;
            width: 350px;
            margin: auto;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
        }

        input {
            width: 90%;
            padding: 10px;
            margin: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }

        button {
            padding: 10px 20px;
            margin: 5px;
            border: none;
            background: #667eea;
            color: white;
            border-radius: 8px;
            cursor: pointer;
        }

        button:hover {
            background: #5a67d8;
        }

        h1 {
            margin-bottom: 10px;
        }

        .result {
            margin-top: 20px;
            font-size: 20px;
            color: green;
        }

        .error {
            margin-top: 20px;
            font-size: 18px;
            color: red;
        }
    </style>
</head>

<body>

<h1>🎓 AI Student Performance Predictor</h1>
<p>Enter student details to predict performance using AI</p>

<div class="container">

<form method="POST">

<input type="number" name="study" min="0" max="12" placeholder="Study Hours (0-12)" required>

<input type="number" name="attendance" min="0" max="100" placeholder="Attendance % (0-100)" required>

<input type="number" name="previous" min="0" max="100" placeholder="Previous Score (0-100)" required>

<button type="submit">Predict</button>
<button type="reset">Reset</button>

</form>

{% if result %}
<div class="result">
📊 Predicted Score: {{result}}
</div>
{% endif %}

{% if status %}
<div class="result">
Performance: {{status}}
</div>
{% endif %}

{% if error %}
<div class="error">
{{error}}
</div>
{% endif %}

</div>

</body>
</html>
"""

# -------------------------------
# ROUTE

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    status = None
    error = None

    if request.method == "POST":
        try:
            study = float(request.form["study"])
            attendance = float(request.form["attendance"])
            previous = float(request.form["previous"])

            if model is not None:
                data = pd.DataFrame({
                    "Study_Hours_per_Day": [study],
                    "Attendance_Percentage": [attendance],
                    "Previous_Exam_Score": [previous]
                })

                pred = model.predict(data)
                result = round(pred[0], 2)

                if result < 40:
                    status = "❌ Fail"
                elif result < 60:
                    status = "⚠ Average"
                elif result < 80:
                    status = "👍 Good"
                else:
                    status = "🏆 Excellent"

            else:
                error = "⚠ Model not loaded. Please check deployment."

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template_string(HTML, result=result, status=status, error=error)

# -------------------------------
# RUN

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)