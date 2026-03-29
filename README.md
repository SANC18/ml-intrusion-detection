# ML-Based Intrusion Detection System

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

A machine learning system that detects network intrusions in real time.
Trained on the NSL-KDD dataset, it flags malicious traffic with
explainable predictions (SHAP) and displays live alerts on a Flask dashboard.

## Features
- Multi-algorithm comparison: Random Forest, LSTM, Isolation Forest
- Real-time packet capture using Scapy
- SHAP explainability — shows WHY a packet was flagged
- Flask dashboard with live alert feed and charts
- Dockerized for easy deployment

## Tech Stack
`Python` `scikit-learn` `TensorFlow` `Scapy` `SHAP` `Flask` `pandas` `Docker`

## Dataset
NSL-KDD — improved version of the classic KDD Cup 1999 dataset.
[Download here](https://www.unb.ca/cic/datasets/nsl.html)

## Project Structure
```
ml-intrusion-detection/
├── data/               # Raw and processed datasets
├── notebooks/          # EDA and model training notebooks
├── src/
│   ├── preprocess.py   # Feature engineering
│   ├── train.py        # Model training
│   ├── predict.py      # Real-time prediction
│   └── capture.py      # Packet capture (Scapy)
├── dashboard/          # Flask web app
├── tests/              # Unit tests
├── requirements.txt
└── README.md
```

## Getting Started
```bash
git clone https://github.com/SANC18/ml-intrusion-detection
cd ml-intrusion-detection
pip install -r requirements.txt
python src/train.py
python dashboard/app.py
```

## Roadmap
- [x] Project structure setup
- [ ] Data preprocessing pipeline
- [ ] Train baseline Random Forest model
- [ ] Add SHAP explainability
- [ ] Build Flask dashboard
- [ ] Add real-time Scapy capture
- [ ] Dockerize

## License
MIT
