from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import HeartDiseaseForm
import pickle
import numpy as np
import os
import sqlite3  # ✅ Import SQLite

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ✅ Define the database model (SQLAlchemy)
class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    chestpaintype = db.Column(db.Integer, nullable=False)
    restingbp = db.Column(db.Integer, nullable=False)
    cholesterol = db.Column(db.Integer, nullable=False)
    fastingbs = db.Column(db.Integer, nullable=False)
    restingecg = db.Column(db.Integer, nullable=False)
    maxhr = db.Column(db.Integer, nullable=False)
    exerciseangina = db.Column(db.Integer, nullable=False)
    oldpeak = db.Column(db.Float, nullable=False)
    st_slope = db.Column(db.Integer, nullable=False)
    prediction = db.Column(db.Integer, nullable=False)
    probability = db.Column(db.Float, nullable=False)

# ✅ Function to Save Prediction using SQLite
def save_prediction(data):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = '''INSERT INTO prediction (age, sex, chestpaintype, restingbp, cholesterol, 
               fastingbs, restingecg, maxhr, exerciseangina, oldpeak, st_slope, prediction, probability) 
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    
    cursor.execute(query, data)
    conn.commit()
    conn.close()

# ✅ Load the ML Model
model_path = "C:\\Users\\Rajendra\\Desktop\\heart_disease_prediction\\best_heart_disease_model(2).pkl"
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
    form = HeartDiseaseForm()

    if request.method == 'POST':
        try:
            if form.validate_on_submit():
                # ✅ Flask-WTF Form Submission
                input_features = np.array([
                    form.age.data, form.sex.data, form.chestpaintype.data,
                    form.restingbp.data, form.cholesterol.data, form.fastingbs.data,
                    form.restingecg.data, form.maxhr.data, form.exerciseangina.data,
                    form.oldpeak.data, form.st_slope.data  # Check this list has 11 values
                ]).reshape(1, -1)

            else:
                # ✅ Manual Form Submission (Ensure all 11 fields are retrieved)
                input_features = np.array([float(request.form[key]) for key in request.form.keys()]).reshape(1, -1)

            # ✅ Ensure correct feature count before prediction
            if input_features.shape[1] != 11:
                return f"Error: Expected 11 features but received {input_features.shape[1]}."

            # ✅ Make Prediction
            prediction = model.predict(input_features)[0]
            probability = round(model.predict_proba(input_features)[0][1] * 100, 2)

            # ✅ Save Prediction to Database
            new_prediction = Prediction(
                age=int(input_features[0][0]), sex=int(input_features[0][1]), chestpaintype=int(input_features[0][2]),
                restingbp=int(input_features[0][3]), cholesterol=int(input_features[0][4]),
                fastingbs=int(input_features[0][5]), restingecg=int(input_features[0][6]),
                maxhr=int(input_features[0][7]), exerciseangina=int(input_features[0][8]),
                oldpeak=float(input_features[0][9]), st_slope=int(input_features[0][10]),
                prediction=prediction, probability=probability
            )
            db.session.add(new_prediction)
            db.session.commit()

            return render_template('result.html', prediction=prediction, probability=probability)

        except Exception as e:
            return f"Error: {e}"

    return render_template('predict.html', form=form)


@app.route('/result', methods=['GET', 'POST'])  # ✅ Allows both GET and POST
def result():
    return render_template('result.html')

@app.route('/predict2', methods=['GET', 'POST'])
def predict2():
    if request.method == 'POST':
        try:
            # Extract input features from the form
            input_features = np.array([float(request.form[key]) for key in request.form.keys()]).reshape(1, -1)

            # Make Prediction
            prediction = model.predict(input_features)[0]
            probability_no = round(model.predict_proba(input_features)[0][0] * 100, 2)
            probability_yes = round(model.predict_proba(input_features)[0][1] * 100, 2)

            # Save Prediction in Database
            new_prediction = Prediction(
                age=int(input_features[0][0]), sex=int(input_features[0][1]), chestpaintype=int(input_features[0][2]),
                restingbp=int(input_features[0][3]), cholesterol=int(input_features[0][4]),
                fastingbs=int(input_features[0][5]), restingecg=int(input_features[0][6]),
                maxhr=int(input_features[0][7]), exerciseangina=int(input_features[0][8]),
                oldpeak=float(input_features[0][9]), st_slope=int(input_features[0][10]),
                prediction=prediction, probability=probability_yes
            )
            db.session.add(new_prediction)
            db.session.commit()

            # Save to SQLite
            data_to_save = tuple(input_features[0]) + (prediction, probability_yes)
            save_prediction(data_to_save)

            return render_template('result2.html', prediction_text=f"Prediction: {prediction}", 
                                   prob_no=probability_no, prob_yes=probability_yes)

        except Exception as e:
            return f"Error: {e}"

    return render_template('predict2.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
