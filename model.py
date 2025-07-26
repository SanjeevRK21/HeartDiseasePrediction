import joblib
import numpy as np

model = joblib.load("best_heart_disease_model (2).pkl")

def predict_heart_disease(data):
    input_data = np.array([[data["age"], data["sex"], data["chestpaintype"], data["restingbp"], data["cholesterol"],
                            data["fastingbs"], data["restingecg"], data["maxhr"], data["exerciseangina"], data["oldpeak"], data["st_slope"]]])
    prediction = model.predict_proba(input_data)[0][1] * 100
    return round(prediction, 2)
