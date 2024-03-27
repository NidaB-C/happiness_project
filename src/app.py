from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and scaler at startup
model = pickle.load(open('../models/random_forest_model.pkl', 'rb'))
scaler = pickle.load(open('../models/scaler.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    # Render the home page with form
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Capture data from the form
    try:
        GDPperCapita = float(request.form['gdp'])
        Family = float(request.form['social'])
        LifeExpectancy = float(request.form['health'])
        Freedom = float(request.form['freedom'])
        NoCorruption = float(request.form['corruption'])
        Generosity = float(request.form['generosity'])
        DystopisResidual = float(request.form['dystopia'])
        
        # Create a feature array for prediction
        features = np.array([[GDPperCapita, Family, LifeExpectancy, Freedom,
                              NoCorruption, Generosity, DystopisResidual]])
                              
        # Scale the feature array
        features_scaled = scaler.transform(features)
        
        # Make a prediction
        prediction = model.predict(features_scaled)
        
        # Interpret the prediction
        prediction_text = 'Happy' if prediction[0] == 1 else 'Not Happy'
        
    except ValueError as e:
        # Handle the error if the input is not a valid float
        prediction_text = f"Invalid input detected. Please enter valid numbers. Error: {e}"

    # Render the page with the prediction results
    return render_template('index.html', prediction_text=f'Prediction: You are {prediction_text}')

if __name__ == '__main__':
    app.run(debug=True)
