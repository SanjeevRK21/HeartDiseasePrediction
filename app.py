from flask import Flask, render_template, request
import pickle
import numpy as np
import sqlite3  # ✅ Import SQLite

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# ✅ Function to Save Prediction using SQLite (database2.db)
def save_prediction(data):
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    
    query = '''INSERT INTO prediction2 (age, sex, chestpaintype, restingbp, cholesterol, 
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
    if request.method == 'POST':
        try:
            input_features = np.array([float(request.form[key]) for key in request.form.keys()]).reshape(1, -1)
            
            # ✅ Ensure correct feature count before prediction
            if input_features.shape[1] != 11:
                return f"Error: Expected 11 features but received {input_features.shape[1]}."
            
            # ✅ Make Prediction
            prediction = int(model.predict(input_features)[0])  # Convert to int to avoid BLOB issue
            probability = float(model.predict_proba(input_features)[0][1])  # No rounding

            return render_template('result.html', prediction=prediction, probability=probability)
        except Exception as e:
            return f"Error: {e}"

    return render_template('predict.html')

@app.route('/predict2', methods=['GET', 'POST'])
def predict2():
    if request.method == 'POST':
        try:
            # Extract input features from the form
            input_features = np.array([float(request.form[key]) for key in request.form.keys()]).reshape(1, -1)

            # Make Prediction
            prediction = int(model.predict(input_features)[0])  # Convert to int
            probability_no = float(model.predict_proba(input_features)[0][0])  # No rounding
            probability_yes = float(model.predict_proba(input_features)[0][1])  # No rounding

            # Save to SQLite (database2.db)
            data_to_save = tuple(input_features[0]) + (prediction, probability_yes)
            save_prediction(data_to_save)

            return render_template('result2.html', prediction_text=f"Prediction: {prediction}", 
                                   prob_no=probability_no, prob_yes=probability_yes)
        except Exception as e:
            return f"Error: {e}"

    return render_template('predict2.html')

@app.route('/save_prediction2', methods=['POST'])
def save_prediction2():
    try:
        # Extract data from the form
        data = (
            request.form['age'], request.form['sex'], request.form['chestpaintype'],
            request.form['restingbp'], request.form['cholesterol'], request.form['fastingbs'],
            request.form['restingecg'], request.form['maxhr'], request.form['exerciseangina'],
            request.form['oldpeak'], request.form['st_slope'], int(request.form['prediction']),  # Convert to int
            float(request.form['probability'])  # Convert to float
        )

        # ✅ Save to database2.db
        conn = sqlite3.connect('database2.db')
        cursor = conn.cursor()

        query = '''INSERT INTO prediction2 (age, sex, chestpaintype, restingbp, cholesterol, 
                   fastingbs, restingecg, maxhr, exerciseangina, oldpeak, st_slope, prediction, probability) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

        cursor.execute(query, data)
        conn.commit()
        conn.close()

        return "Prediction saved successfully! <br><a href='/predict2'>Go Back</a>"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
