import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Simulate some financial data for training
# You would replace this with your actual data loading and preprocessing logic
data = {
    'Income': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],
    'Rent': [1500, 1800, 2000, 2200, 2500, 2700, 3000, 3200, 3400, 3600],
    'Utilities': [200, 220, 240, 260, 280, 300, 320, 340, 360, 380],
    'Groceries': [300, 320, 340, 360, 380, 400, 420, 440, 460, 480],
    'Savings': [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500]  # Target variable
}

df = pd.DataFrame(data)

# Define features and target variable
X = df[['Income', 'Rent', 'Utilities', 'Groceries']]
y = df['Savings']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Save the trained model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")


