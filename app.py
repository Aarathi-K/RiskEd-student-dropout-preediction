from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("dropout_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    attendance = float(request.form["attendance"])
    avg_marks = float(request.form["avg_marks"])
    fee_delay = int(request.form["fee_delay"])
    backlogs = int(request.form["backlogs"])
    extracurricular = float(request.form["extracurricular"])

    input_data = np.array([[attendance, avg_marks, fee_delay, backlogs, extracurricular]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        risk = "High Dropout Risk"
    else:
        risk = "Low Dropout Risk"

    return render_template(
        "result.html",
        prediction=risk,
        probability=round(probability * 100, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)

