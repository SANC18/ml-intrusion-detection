"""
ML-Based Intrusion Detection System — Flask Dashboard
Author: Sanchita Jain
"""

from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)

# ─── Load models on startup ───────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR  = os.path.join(BASE_DIR, 'src')

with open(os.path.join(SRC_DIR, 'rf_model.pkl'), 'rb') as f:
    rf_model = pickle.load(f)

with open(os.path.join(SRC_DIR, 'xgb_model.pkl'), 'rb') as f:
    xgb_model = pickle.load(f)

with open(os.path.join(SRC_DIR, 'scaler.pkl'), 'rb') as f:
    scaler = pickle.load(f)

with open(os.path.join(SRC_DIR, 'feature_names.pkl'), 'rb') as f:
    feature_names = pickle.load(f)

print(f"Models loaded. Features: {feature_names}")

# ─── In-memory alert log ──────────────────────────────────────────────────────
alerts = []

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    """Main dashboard page."""
    return render_template('index.html', feature_names=feature_names)


@app.route('/predict', methods=['POST'])
def predict():
    """
    Accept JSON with feature values, return prediction.

    Expected JSON format:
    {
        "model": "random_forest",   # or "xgboost"
        "features": [val1, val2, ...]   # 20 feature values in order
    }
    """
    data = request.get_json()

    if not data or 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400

    features = data.get('features', [])
    model_name = data.get('model', 'random_forest')

    if len(features) != len(feature_names):
        return jsonify({
            'error': f'Expected {len(feature_names)} features, got {len(features)}'
        }), 400

    # Scale features
    features_array = np.array(features).reshape(1, -1)
    features_scaled = scaler.transform(features_array)

    # Select model
    model = rf_model if model_name == 'random_forest' else xgb_model

    # Predict
    prediction = int(model.predict(features_scaled)[0])
    probability = float(model.predict_proba(features_scaled)[0][1])

    result = 'ATTACK' if prediction == 1 else 'NORMAL'
    confidence = round(probability * 100, 2) if prediction == 1 else round((1 - probability) * 100, 2)

    # Log alert
    alert = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'result': result,
        'confidence': confidence,
        'model': model_name,
        'features': dict(zip(feature_names, features))
    }
    alerts.append(alert)

    return jsonify({
        'prediction': prediction,
        'result': result,
        'confidence': confidence,
        'probability': round(probability, 4),
        'model_used': model_name,
        'timestamp': alert['timestamp']
    })


@app.route('/alerts')
def get_alerts():
    """Return all logged alerts."""
    return jsonify(alerts[-50:])  # Return last 50 alerts


@app.route('/stats')
def get_stats():
    """Return summary statistics."""
    total = len(alerts)
    attacks = sum(1 for a in alerts if a['result'] == 'ATTACK')
    normal = total - attacks

    return jsonify({
        'total_predictions': total,
        'attacks_detected': attacks,
        'normal_traffic': normal,
        'attack_rate': round((attacks / total * 100), 2) if total > 0 else 0
    })


@app.route('/features')
def get_features():
    """Return list of required feature names."""
    return jsonify({'features': feature_names})


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'running', 'models_loaded': True})


# ─── Run ──────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
