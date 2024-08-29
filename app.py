from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from finance_analysis import analyze_finances  # Ensure this is correctly implemented
import matplotlib.pyplot as plt
import io
import base64

# Initialize the Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow CORS for all origins

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()  # Parse JSON data from the request
        income = float(data.get('income', 0))
        rent = float(data.get('rent', 0))
        utilities = float(data.get('utilities', 0))
        groceries = float(data.get('groceries', 0))

        # Analyze financial data
        total_income, total_expenses, suggestion = analyze_finances(income, rent, utilities, groceries)

        # Generate pie chart and convert to base64
        pie_chart_base64 = create_pie_chart_base64(rent, utilities, groceries)

        response = {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "suggestion": suggestion,
            "pie_chart": pie_chart_base64
        }

        return jsonify(response)

    except Exception as e:
        print(f"Error: {e}")  # Log error for debugging
        return jsonify({'error': 'An error occurred while analyzing data.'}), 500

def create_pie_chart_base64(rent, utilities, groceries):
    # Data for the pie chart
    labels = ['Rent', 'Utilities', 'Groceries']
    sizes = [rent, utilities, groceries]
    colors = ['gold', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)  # Explode the first slice

    # Plot
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)

    # Convert image to base64
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

    return img_base64

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.get_json().get('message', '')
    
    # Placeholder for AI chatbot logic
    response = "Sorry, I'm just a simple finance manager assistant. How can I help you?"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)



