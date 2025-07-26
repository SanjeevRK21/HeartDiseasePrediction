import numpy as np
import pickle

# Load the trained model
model_path = "C:\\Users\\Rajendra\\Desktop\\heart_disease_prediction\\best_heart_disease_model(2).pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Test input (replace with actual expected input format)
sample_input = np.array([[45, 1, 1, 120, 200, 0, 1, 150, 0, 1.2, 2]])  # Example input values

# Ensure input shape matches what the model expects
prediction = model.predict(sample_input)
probabilities = model.predict_proba(sample_input)

print(f"Prediction: {prediction[0]}")
print(f"Probabilities: {probabilities[0][0]*100:.2f}% (No Disease), {probabilities[0][1]*100:.2f}% (Disease)")
