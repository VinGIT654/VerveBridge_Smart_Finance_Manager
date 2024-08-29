import React, { useState } from 'react';

const FinanceForm = () => {
    const [income, setIncome] = useState('');
    const [rent, setRent] = useState('');
    const [utilities, setUtilities] = useState('');
    const [groceries, setGroceries] = useState('');
    const [predictedSavings, setPredictedSavings] = useState(null);
    const [chatInput, setChatInput] = useState('');
    const [chatResponse, setChatResponse] = useState('');
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        try {
            const response = await fetch('http://localhost:5000/api/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    income: parseFloat(income),
                    rent: parseFloat(rent),
                    utilities: parseFloat(utilities),
                    groceries: parseFloat(groceries),
                }),
            });
            const data = await response.json();
            if (response.ok) {
                setResult(data);
                setPredictedSavings(data.predicted_savings);
            } else {
                setError('An error occurred while analyzing data.');
                console.error('Error analyzing data', data.error);
            }
        } catch (error) {
            setError('An error occurred while analyzing data.');
            console.error('Error analyzing data', error);
        }
    };

    const handleChatSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://localhost:5000/chatbot', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: chatInput }),
            });
            const data = await response.json();
            if (response.ok) {
                setChatResponse(data.response);
            } else {
                console.error('Error getting chatbot response', data.error);
            }
        } catch (error) {
            console.error('Error getting chatbot response', error);
        }
    };

    return (
        <div>
            <h1>Smart Finance Manager</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Income:
                    <input
                        type="number"
                        placeholder="Income"
                        value={income}
                        onChange={(e) => setIncome(e.target.value)}
                    />
                </label>
                <label>
                    Rent:
                    <input
                        type="number"
                        placeholder="Rent"
                        value={rent}
                        onChange={(e) => setRent(e.target.value)}
                    />
                </label>
                <label>
                    Utilities:
                    <input
                        type="number"
                        placeholder="Utilities"
                        value={utilities}
                        onChange={(e) => setUtilities(e.target.value)}
                    />
                </label>
                <label>
                    Groceries:
                    <input
                        type="number"
                        placeholder="Groceries"
                        value={groceries}
                        onChange={(e) => setGroceries(e.target.value)}
                    />
                </label>
                <button type="submit">Analyze</button>
            </form>

            {result && (
                <div className="analysis-result">
                    <h2>Analysis Result</h2>
                    <p>Total Income: ${result.total_income}</p>
                    <p>Total Expenses: ${result.total_expenses}</p>
                    <p>Suggestions: {result.suggestion}</p>
                    <img src={`data:image/png;base64,${result.pie_chart}`} alt="Expenses Pie Chart" />
                    <p>Prediction: ${predictedSavings ? predictedSavings.toFixed(2) : 'N/A'}</p>
                </div>
            )}

            {error && <p className="error-message">{error}</p>}

            <form onSubmit={handleChatSubmit}>
                <input
                    type="text"
                    placeholder="Ask AI Assistant"
                    value={chatInput}
                    onChange={(e) => setChatInput(e.target.value)}
                />
                <button type="submit">Ask</button>
            </form>
            {chatResponse && (
                <div className="chat-response">AI Assistant: {chatResponse}</div>
            )}
        </div>
    );
};

export default FinanceForm;








