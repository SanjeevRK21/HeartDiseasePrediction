from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Load the ML Model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "ML_model", "best_heart_disease_model.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/diseases")
def diseases():
    return render_template("diseases.html")


@app.route("/model_info")
def model_info():
    return render_template("model.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get input features
            input_features = np.array(
                [float(request.form[key]) for key in request.form.keys()]
            ).reshape(1, -1)

            # Ensure correct number of features
            if input_features.shape[1] != 11:
                return f"Error: Expected 11 features but received {input_features.shape[1]}."

            # Make prediction
            prediction = int(model.predict(input_features)[0])
            probability_no = float(model.predict_proba(input_features)[0][0])
            probability_yes = float(model.predict_proba(input_features)[0][1])

            return render_template(
                'result.html',
                prediction_text=prediction,
                prob_no=probability_no,
                prob_yes=probability_yes
            )

        except Exception as e:
            return f"Error: {e}"

    return render_template('predict.html')


@app.route('/predict2', methods=['GET', 'POST'])
def predict2():
    if request.method == 'POST':
        try:
            # Get input features
            input_features = np.array(
                [float(request.form[key]) for key in request.form.keys()]
            ).reshape(1, -1)

            # Make prediction
            prediction = int(model.predict(input_features)[0])
            probability_no = float(model.predict_proba(input_features)[0][0])
            probability_yes = float(model.predict_proba(input_features)[0][1])

            return render_template(
                'result2.html',
                prediction_text=prediction,
                prob_no=probability_no,
                prob_yes=probability_yes
            )

        except Exception as e:
            return f"Error: {e}"

    return render_template('predict2.html')


if __name__ == "__main__":
    app.run(debug=True)