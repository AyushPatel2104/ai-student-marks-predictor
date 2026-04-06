from flask import Flask, render_template, request, redirect, url_for, jsonify
import pickle

app = Flask(__name__)

# Load model
import os

model_path = os.path.join(os.path.dirname(__file__), 'models', 'pipeline_model.pkl')
model = pickle.load(open(model_path, 'rb'))

USERNAME = "admin"
PASSWORD = "admin123"

@app.route('/', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid Credentials"
    return render_template('login.html', error=error)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    features = [[
        float(data['hours']),
        float(data['attendance']),
        float(data['sleep']),
        float(data['assignments']),
        float(data['previous'])
    ]]

    try:
        prediction = model.predict(features)[0]
        score = round(float(prediction), 2)
    except:
        score = 65

    if score > 75:
        status = "Excellent"
        risk = "Low Risk"
        grade = "A"
    elif score > 50:
        status = "Average"
        risk = "Medium Risk"
        grade = "B"
    else:
        status = "Below Average"
        risk = "High Risk"
        grade = "D"

    return jsonify({
        "score": score,
        "status": status,
        "risk": risk,
        "grade": grade
    })


if __name__ == '__main__':
    app.run(debug=True)