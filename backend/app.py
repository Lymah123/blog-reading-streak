from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app)
# Simulated database
reading_log = {}

# Add a daily reading stat
@app.route('/log', methods=['POST'])
def log_reading():
    data = request.json
    date = data.get('date') or datetime.today().strftime('%Y-%m-%d')
    count = data.get('count', 0)
    reading_log[date] = count
    return jsonify({"message": "Reading logged!", "data": reading_log}), 201

# Calculate streak
@app.route('/streak', methods=['GET'])
def get_streak():
    streak = 0
    max_streak = 0
    current_date = datetime.today().date()

    for i in range(30):  # Check the past 30 days
        date_str = (current_date - timedelta(days=i)).strftime('%Y-%m-%d')
        if date_str in reading_log and reading_log[date_str] > 0:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0

    return jsonify({"current_streak": streak, "max_streak": max_streak, "log": reading_log})

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
