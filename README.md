# Cardio-Kawaii: AI-Powered Heart Disease Prediction
A full-stack Flask + Machine Learning web application that predicts the likelihood of heart disease using clinical data, combined with an interactive, visually rich frontend for education and user engagement.

## Overview 
This project integrates:  
- Machine Learning model for prediction
- Flask backend for inference
- Tailwind CSS frontend with animated UI
- Data-driven health insights and visual explanations
Users can:  
- Learn about heart diseases
- Understand risk factors
- Input health parameters
- Get real-time AI predictions with probabilities
  
## Features
### Interactive Homepage
- Futuristic UI with animations and heart-health awareness
- Displays fun facts and global statistics  
👉 Implemented in:  [`index.html`](./index.html)

### Heart Disease Awareness Module
- Explains different heart diseases
- Shows risk levels (10% – 90%)
- Includes prevention tips (diet, exercise, sleep, etc.)  
👉 Implemented in: [`diseases.html`](./diseases.html)

### AI Model Explanation Page
- Explains ML pipeline:
  - Data preprocessing 
  - Feature selection
  - Model training

- Shows:
  - Accuracy: 92%
  - Confusion Matrix
  - ROC Curve (~0.96 AUC)
  - Precision-Recall insights  
👉 Implemented in: [`model.html`](./model.html)

### Prediction Interface
- Advanced UI Form
  - Modern animated AI-themed interface
  - Collects 11 clinical features (age, cholesterol, ECG, etc.)  
👉 Implemented in: [`predict.html`](./predict.html)

- Simple Form (Fallback)
  - Minimal UI version for reliability  
👉 Implemented in: [`predict2.html`](./predict2.html)

### Prediction Results Dashboard
- Displays:
  - Risk classification (High / Low)
  - Probability scores
- Dynamic UI feedback (color-coded health status)  
- Includes fallback to Colab notebook  
👉 Implemented in: [`result.html`](./result.html)

## Backend Architecture
### Flask Server
- Handles routing
- prediction
- template rendering    
👉 Implemented in: [`index.py`](./index.py)

## Key Routes
| Route	| Description |
| --- | --- |
| `/`	 | Homepage |
| `/diseases` |	Heart disease awareness |
| `/model_info`	| ML model explanation |
| `/predict`	| Main prediction form |
| `/predict2`	| Alternative prediction form |
| `/result`	| Prediction output |

## Machine Learning Model
- Loaded via pickle (.pkl)
- Trained on clinical dataset
- Uses:
  - Decision Tree / Random Forest approach
- Input: 11 features
- Output:
  - Binary prediction
  - Probability scores

## System Workflow
```
User Input → Flask Backend → ML Model → Prediction → Probability → UI Display
```

## Project Structure
```
.
├── templates/
│   ├── index.html
│   ├── diseases.html
│   ├── model.html
│   ├── predict.html
│   ├── predict2.html
│   ├── result.html
│
├── ML_model/
│   └── best_heart_disease_model.pkl
│
├── index.py
└── README.md
```

## Installation
```
git clone https://github.com/SanjeevRK21/HeartDiseasePrediction.git
cd cardio-kawaii

pip install flask numpy scikit-learn
```

## Running the App
```
python index.py
```
Then open:
```
http://127.0.0.1:5000/
```

## Example Prediction Flow
- User enters:
  - Age, BP, Cholesterol, ECG, etc.
-  Flask collects inputs → converts to NumPy array
- Model predicts:  
  - 0 → No Disease
  - 1 → High Risk
- Probabilities displayed in UI

## Tech Stack
### Frontend
- HTML5
- Tailwind CSS
- Animations (CSS keyframes, gradients, effects)

### Backend
- Flask
- NumPy
- Machine Learning
- Scikit-learn
- Pickle (model persistence)

## Key Highlights
- Combines education + prediction + visualization
- Real-time ML inference via Flask
- Highly interactive and modern UI
- Dual prediction interfaces (robust fallback)
- Probability-based decision support

## Future Improvements
- Add user authentication
- Store prediction history
- Deploy on cloud (AWS / Render)
- Integrate wearable health data
- Improve model with deep learning

## Disclaimer
This application is for educational purposes only and not a substitute for professional medical advice.

## Author
Sanjeev Raj
