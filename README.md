# Laptop Recommendation System

This project is a Machine Learning-based web application designed to help users find the most suitable laptops based on their personal preferences. 
Users rank how important different laptop features are to them (e.g., CPU, GPU, RAM, Weight), and the system returns the top 5 matching laptops using a trained ML model.

---

## Features

- **React Frontend**: Interactive UI with sliders to rank features
- **Flask Backend**: Receives input and serves predictions
- **Machine Learning**: Trained Random Forest Regressors generate aspect-level rankings for each laptop
- **Smart Matching**: Each laptop is matched based on how well it satisfies the user’s weighted criteria
- **Clean Dataset**: 980 laptops cleaned, processed, and scored for multiple aspects
- **EDAS Integration Ready**: (Optional) External Decision Analysis support by Industrial Engineering team

---

## How It Works

1. User ranks importance of features (Weight, CPU, GPU, Price, etc.)
2. System uses pre-ranked aspect dataset (`aspect_data.csv`)
3. Backend filters and scores laptops
4. Top 5 matches are returned with details like:
   - CPU, GPU, RAM, Screen Size, OS, Brand, Price, etc.

---

## Tech Stack

| Component     | Technology       |
|---------------|------------------|
| Frontend      | React.js         |
| Backend       | Flask (Python)   |
| ML Model      | RandomForest     |
| Data Format   | CSV              |
| Hosting       | Localhost        |

---

## Usage Instructions

1. Clone the repository

git clone https://github.com/iamsadygov/capstonese.git

2. Setup Backend (Python 3.10+ required)

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate (Linux/macOS)
.\venv\Scripts\activate (Windows)

Install dependencies:
pip install flask flask-cors pandas numpy scikit-learn

Run the backend server:
cd backend
python api.py

3. Set up the frontend (node.js and npm required)
Navigate to the frontend directory:
cd frontend

Install dependencies:
npm install

Start the frontend app:
npm start

This will start the React app at http://localhost:3000
