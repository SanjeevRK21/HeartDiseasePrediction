import pickle

try:
    with open("best_heart_disease_model(1).pkl", "rb") as model_file:
        model = pickle.load(model_file)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error: {e}")
