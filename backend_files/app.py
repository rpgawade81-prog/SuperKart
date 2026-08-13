
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, jsonify

# Create Flask app
app = Flask(__name__)

# Load the model
model = joblib.load('xgb_tuned_model.joblib')

@app.route('/')
def home():
    return "Welcome to the SuperKart Sales Prediction API! Use the /predict endpoint to make predictions."

# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get data from POST request
            data = request.get_json()

            # Convert JSON data to a pandas DataFrame
            df = pd.DataFrame([data])

            # Make prediction
            prediction = model.predict(df)

            # Return the prediction as JSON
            return jsonify({'prediction': prediction[0]})

        except Exception as e:
            return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
