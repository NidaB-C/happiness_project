from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import pickle

# Load the dataset
data_cleaned = pd.read_csv('../data/processed/cleaned_happiness_data.csv')

# Define features and target
features = data_cleaned.drop(['HappinessIndicator'], axis=1)
target = data_cleaned['HappinessIndicator']

# Scale the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Save the scaler for future use
with open('../models/scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

# Create the Random Forest classifier instance and fit the model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Save the Random Forest model
with open('../random_forest_model.pkl', 'wb') as model_file:
    pickle.dump(rf_model, model_file)
