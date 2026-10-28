# Student GPA Performance Predictor

> **"Early Intervention. Academic Insights. Powered by Supervised Machine Learning."**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-black.svg)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E.svg)](https://scikit-learn.org/)

Student GPA Performance Predictor is a full-stack educational data science platform and machine learning system. It empowers educators, academic counselors, and students to forecast Grade Point Averages (GPA) from behavioral, demographic, and study habit predictors (study time, class attendance, parental support, tutoring, and extracurriculars). By identifying at-risk academic trajectories early, institutions can deliver personalized guidance before semester final examinations.

---

## 🚀 Key Features

1. **Supervised Regression & Classification Engine**: Trains supervised machine learning models on multidimensional student metrics to output calibrated GPA predictions and performance tiers.
2. **Interactive Student Lookup by ID**: Real-time query tool enabling counselors to search records by Student ID (`1001`, `1002`, etc.) to review academic history and model predictions.
3. **Dual Serving Architecture**: Ships with both an interactive command-line interface (`student_gpa_prediction.py`) and a production-ready Flask REST backend with CORS support (`flask_app.py`).
4. **Modern Responsive Frontend**: Interactive web interface (`index.html`) featuring real-time search inputs, student profile cards, metric badges, and prediction charts.
5. **Comprehensive Feature Analysis**: Incorporates demographic indicators, weekly study hours, attendance rates, parental education level, tutoring history, and extracurricular participation.
6. **Executive Documentation Included**: Complete project briefs and research documentation preserved in `docs/` for academic evaluation.

---

## 🛠 Tech Stack

- **Language**: Python 3.10+
- **Machine Learning**: Scikit-Learn (`LinearRegression`, `RandomForest`, `LabelEncoder`), NumPy
- **Data Engineering**: Pandas
- **Backend API**: Flask, Flask-CORS, Waitress (production WSGI server)
- **Frontend**: HTML5, Vanilla JavaScript, CSS3
- **Testing**: Pytest automated regression suite

---

## 🏗 Architecture & Directory Structure

```
Student_performance_prediction/
├── docs/                     # Project research papers & evaluation briefs
│   ├── Student_Performance_Predictor_Document.docx
│   └── Student_Performance_Predictor_Document.pdf
├── tests/
│   └── test_model.py         # Automated dataset and ML pipeline unit tests
├── flask_app.py              # Flask REST API server and CORS handlers
├── student_gpa_prediction.py # Interactive CLI and model training engine
├── student_performance_data.csv # Primary student dataset
├── index.html                # Single-page client interface
├── requirements.txt          # Python dependencies
├── .gitattributes            # Linguist language definitions
├── .gitignore                # Ignored cache and virtualenv files
├── LICENSE                   # MIT License
└── README.md                 # Project documentation
```

---

## ⚡ Getting Started

### Prerequisites

- Python `3.10` or higher
- `pip` package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/chakriburidi237-crypto/Student_performance_prediction.git
   cd Student_performance_prediction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the CLI Tool

```bash
python student_gpa_prediction.py
```
Follow the interactive prompt to search any Student ID (e.g. `1001` - `3392`).

### Running the Web Server

```bash
python flask_app.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) or launch `index.html` in your browser.

---

## 🧪 Automated Testing

Run the automated test suite to verify dataset integrity and model loading:

```bash
pytest tests/ -v
```

Expected output:
```
tests/test_model.py::test_dataset_exists_and_valid PASSED
tests/test_model.py::test_model_module_importable PASSED
======================== 2 passed in 0.44s ========================
```

---

## 📄 License and Copyright\n\nAll rights reserved © 2026 Chakradhar Buridi.

