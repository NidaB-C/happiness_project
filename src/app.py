from flask import Flask, request, render_template
from sqlalchemy import create_engine
import pickle
import numpy as np
import sql.load_to_sql as load_to_sql

app = Flask(__name__)

# Load the model and scaler at startup
model = pickle.load(open('../models/random_forest_model.pkl', 'rb'))
scaler = pickle.load(open('../models/scaler.pkl', 'rb'))

# Load data into SQLite database
load_to_sql.cleaned_data

# Create sqlalchemy engine
engine = create_engine('sqlite:///../sql/happiness_data.sqlite')

@app.route('/', methods=['GET'])
def home():
    # Render the home page with form
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Capture data from the form
     try:
        GDPperCapita = float(int(request.form['gdp'])/5)
        Family = float(int(request.form['social'])/5)
        LifeExpectancy = float(int(request.form['health'])/5)
        Freedom = float(int(request.form['freedom'])/10)
        NoCorruption = float(int(request.form['corruption'])/10)
        Generosity = float(int(request.form['generosity'])/10)
        DystopisResidual = float(int(request.form['dystopia'])/10)
        
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
        prediction = f"Invalid input detected. Please enter valid numbers. Error: {e}"

    # Render the page with the prediction results
     return render_template('result.html', prediction_text=f'Prediction: You are {prediction_text}')

if __name__ == '__main__':
    app.run(debug=True)
