import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# finance_analysis.py

def analyze_finances(income, rent, utilities, groceries):
    # Perform financial calculations
    total_expenses = rent + utilities + groceries
    savings = income - total_expenses
    
    if savings < 0:
        suggestion = "Uh-oh! You're spending more than you're earning. Consider reducing expenses."
    elif savings == 0:
        suggestion = "You're breaking even. Look for areas to optimize spending."
    else:
        suggestion = "Great job! You're saving money each month. Consider investing or increasing savings."
    
    return income, total_expenses, suggestion

# Example usage
if __name__ == "__main__":
    income = 75000
    rent = 2000
    utilities = 300
    groceries = 350

    savings = analyze_finances(income, rent, utilities, groceries)
    print(f"Predicted Savings: {savings}")



