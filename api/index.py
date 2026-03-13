from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Tell Flask where templates and static folders are
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

app.config['SECRET_KEY'] = 'your_secret_key_here'


# -------------------------------
# Load the ML model once on startup
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "..", "ML_model", "best_heart_disease_model.pkl")

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


# -------------------------------
# Health check route
# -------------------------------
@app.route("/health")
def health():
    return "Server running successfully"


# -------------------------------
# Homepage
# -------------------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/diseases")
def diseases():
    return render_template("diseases.html")


@app.route("/model_info")
def model_info():
    return render_template("model.html")


# -------------------------------
# Main prediction route
# -------------------------------
@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':
        try:

            input_features = np.array(
                [float(request.form[key]) for key in request.form.keys()]
            ).reshape(1, -1)

            if input_features.shape[1] != 11:
                return f"Error: Expected 11 features but received {input_features.shape[1]}."

            prediction = int(model.predict(input_features)[0])
            probability_no = float(model.predict_proba(input_features)[0][0])
            probability_yes = float(model.predict_proba(input_features)[0][1])

            if prediction == 1:
                prediction_text = "High Risk of Heart Disease"
            else:
                prediction_text = "Low Risk of Heart Disease"

            return render_template(
                "result.html",
                prediction_text=prediction_text,
                prob_no=probability_no,
                prob_yes=probability_yes
            )

        except Exception as e:
            return f"Error during prediction: {e}"

    return render_template("predict.html")


# -------------------------------
# Alternate prediction route
# -------------------------------
@app.route('/predict2', methods=['GET', 'POST'])
def predict2():

    if request.method == 'POST':
        try:

            input_features = np.array(
                [float(request.form[key]) for key in request.form.keys()]
            ).reshape(1, -1)

            prediction = int(model.predict(input_features)[0])
            probability_no = float(model.predict_proba(input_features)[0][0])
            probability_yes = float(model.predict_proba(input_features)[0][1])

            if prediction == 1:
                prediction_text = "High Risk of Heart Disease"
            else:
                prediction_text = "Low Risk of Heart Disease"

            return render_template(
                "result2.html",
                prediction_text=prediction_text,
                prob_no=probability_no,
                prob_yes=probability_yes
            )

        except Exception as e:
            return f"Error during prediction: {e}"

    return render_template("predict2.html")