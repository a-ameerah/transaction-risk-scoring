# Transaction Risk Scoring Model

A simple Python-based model for calculating and visualizing transaction risks using weighted factors such as amount, account history, unusual location, and unusual time.

## Features
- Normalizes transaction data for fair comparison
- Applies weighted scoring for different risk factors
- Classifies transactions into **High** or **Low** risk
- Visualizes risk distribution using Seaborn

## Technologies Used
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn

## How It Works
1. Reads transaction data from a CSV file
2. Normalizes numeric columns (`amount`, `account_history`)
3. Applies a weighted risk formula: total_risk = amount_risk + history_risk + time_risk + location_risk
4. Flags transactions with risk score > 0.5 as **High Risk**

## Installation
```bash
git clone https://github.com/a-ameerah/transaction-risk-scoring.git
cd transaction-risk-scoring
pip install -r requirements.txt

## Usage
python src/risk_model.py
