# ML-Based Intrusion Detection System

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)
![Accuracy](https://img.shields.io/badge/Accuracy-99.98%25-brightgreen)

A machine learning system that detects network intrusions by 
training and comparing 5 classifiers on the KDD Cup 99 dataset.
Includes SHAP explainability, ROC curves, and a Flask dashboard
for real-time alert monitoring.

## Results

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Random Forest | 99.98% | 1.00 | 0.99 | 1.00 |
| XGBoost | TBD | TBD | TBD | TBD |
| Decision Tree | TBD | TBD | TBD | TBD |
| KNN | TBD | TBD | TBD | TBD |
| SVM | TBD | TBD | TBD | TBD |

## Features
- 5 ML classifiers trained and compared
- SMOTE oversampling for class imbalance
- Statistical feature selection (top 20 features)
- SHAP explainability for best 2 models
- ROC curve comparison
- Confusion matrices for all models
- Flask dashboard with live alert feed
- Dockerized deployment

## Tech Stack
`Python` `scikit-learn` `XGBoost` `SHAP` `Flask` `pandas`
`numpy` `matplotlib` `seaborn` `imbalanced-learn` `Docker`

## Dataset
KDD Cup 99 — loaded via scikit-learn's built-in `fetch_kddcup99`
(SA subset, 10% sample — 100,655 records, 42 features)

## Project Structure
ml-intrusion-detection/
├── data/               # Raw datasets
├── notebooks/
│   └── 01_data_exploration.ipynb  # All EDA + model training
├── src/
│   ├── rf_model.pkl    # Saved Random Forest model
│   ├── xgb_model.pkl   # Saved XGBoost model
│   ├── scaler.pkl      # StandardScaler
│   ├── feature_names.pkl
│   └── model_results.csv
├── dashboard/
│   └── app.py          # Flask web app
├── tests/
├── requirements.txt
└── README.md

## Getting Started
```bash
git clone https://github.com/SANC18/ml-intrusion-detection
cd ml-intrusion-detection
pip install -r requirements.txt
jupyter notebook notebooks/01_data_exploration.ipynb
```

## Roadmap
- [x] Load and explore KDD Cup 99 dataset
- [x] Binary label encoding
- [x] Feature encoding and preprocessing
- [x] Train/test split and StandardScaler
- [x] Train Random Forest (99.98% accuracy)
- [x] SHAP explainability
- [x] Confusion matrix
- [x] Save model with pickle
- [ ] Add SMOTE for class imbalance
- [ ] Feature selection (top 20)
- [ ] Train Decision Tree
- [ ] Train XGBoost
- [ ] Train KNN
- [ ] Train SVM
- [ ] Model comparison chart
- [ ] ROC curves for all models
- [ ] SHAP for XGBoost
- [ ] Flask dashboard
- [ ] Dockerize

## License
MIT