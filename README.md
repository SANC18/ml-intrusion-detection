# ML-Based Intrusion Detection System

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Accuracy](https://img.shields.io/badge/Best%20Accuracy-99.98%25-brightgreen)

A machine learning system that detects network intrusions by training and
comparing 5 classifiers on the KDD Cup 99 dataset. Includes SMOTE
oversampling, statistical feature selection, SHAP explainability, ROC
curves, and a Flask dashboard for real-time alert monitoring.

---

## Results

| Model | Accuracy | Precision | Recall | F1-Score | Train Time |
|---|---|---|---|---|---|
| **Random Forest** | **99.98%** | **99.99%** | **99.97%** | **99.98%** | 6.42s |
| **XGBoost** | **99.98%** | **99.97%** | **99.98%** | **99.98%** | 0.68s |
| Decision Tree | 99.96% | 99.96% | 99.96% | 99.96% | 0.47s |
| KNN | 99.92% | — | — | — | 0.02s |
| SVM | 99.61% | — | — | — | 22.60s |

**Best models: Random Forest and XGBoost** (tied at 99.98%)
XGBoost is recommended for production — same accuracy, 9x faster training.

---

## Features
- 5 ML classifiers trained and compared
- SMOTE oversampling for class imbalance (28.8:1 ratio fixed)
- Statistical feature selection — top 20 features from 41
- SHAP explainability for Random Forest and XGBoost
- ROC curves and confusion matrices for all 5 models
- Flask dashboard with live alert feed and prediction API
- Dockerized for easy deployment

---

## Tech Stack
`Python` `scikit-learn` `XGBoost` `SHAP` `Flask` `pandas`
`numpy` `matplotlib` `seaborn` `imbalanced-learn` `Docker`

---

## Dataset
KDD Cup 99 — loaded via scikit-learn's built-in `fetch_kddcup99`
(SA subset, 10% sample — 100,655 records, 42 features)
After SMOTE: 194,556 records, balanced 50/50

---

## Project Structure
```
ml-intrusion-detection/
├── data/                        # Raw datasets
├── notebooks/
│   └── 01_data_exploration.ipynb  # Complete ML pipeline
├── src/
│   ├── rf_model.pkl             # Saved Random Forest model
│   ├── xgb_model.pkl            # Saved XGBoost model
│   ├── scaler.pkl               # StandardScaler
│   ├── feature_names.pkl        # Top 20 feature names
│   └── model_results.csv        # Comparison results
├── dashboard/
│   ├── app.py                   # Flask web app
│   └── templates/
│       └── index.html           # Dashboard UI
├── tests/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Getting Started

### Run locally
```bash
git clone https://github.com/SANC18/ml-intrusion-detection
cd ml-intrusion-detection
pip install -r requirements.txt
python dashboard/app.py
# Open http://localhost:5000
```

### Run with Docker
```bash
docker build -t ids-dashboard .
docker run -p 5000:5000 ids-dashboard
# Open http://localhost:5000
```

---

## Roadmap
- [x] Load and explore KDD Cup 99 dataset
- [x] Binary label encoding (normal=0, attack=1)
- [x] Feature encoding and preprocessing
- [x] SMOTE oversampling for class imbalance
- [x] Statistical feature selection (top 20 features)
- [x] Train/test split and StandardScaler
- [x] Train all 5 classifiers
- [x] Model comparison chart
- [x] ROC curves for all 5 models
- [x] Confusion matrices for all 5 models
- [x] SHAP explainability for RF and XGBoost
- [x] Save all models with pickle
- [x] Flask dashboard with prediction API
- [x] Docker deployment
- [ ] Deploy to Render (live URL)

---

## License
MIT
