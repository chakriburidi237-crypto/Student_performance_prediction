<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4facfe,100:00f2fe&height=200&section=header&text=Student%20Performance%20Predictor&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=ML-Powered%20GPA%20Prediction%20%7C%20Full%20Stack%20%7C%20React%20%2B%20Flask&descAlignY=55&descSize=17" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)

<br/>

> ### 📊 *"Predict student academic performance using Machine Learning"*
> **ML Model • REST API • React Frontend • Real Dataset**

<br/>

![Visitor Count](https://komarev.com/ghpvc/?username=chakriburidi237-crypto&color=4facfe&style=flat-square&label=Profile+Views)

---

</div>

## 🎯 What Is This Project?

**Student Performance Predictor** is a full-stack machine learning application that predicts a student's **GPA** based on key academic and behavioral features. Built with a custom **Linear Regression model using Gradient Descent**, a **Flask REST API backend**, and a **React + Vite frontend**.

Enter a Student ID → Get instant GPA prediction + full student profile analytics.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Student ID Lookup** | Search any student by ID instantly |
| 📊 **GPA Prediction** | ML model predicts GPA with high accuracy |
| 🎓 **Grade Classification** | Classifies student into grade categories |
| 📋 **Full Profile Display** | Shows all student attributes in a clean card UI |
| ⚡ **Fast API** | Flask REST API with CORS support |
| 🎨 **Modern UI** | Clean React frontend with responsive design |
| 🧹 **Data Preprocessing** | Handles missing values, duplicates, encoding |

---

## 🏗️ Project Structure

```
Student_performance_prediction-main/
│
├── STUDENT GPA PREDICTOR/
│   ├── student_gpa_prediction.py   # Core ML model (Gradient Descent)
│   ├── flask_app.py                # Flask app entry point
│   ├── diagnose.py                 # Diagnostic utilities
│   ├── Student_performance_data.csv # Dataset (2000+ students)
│   ├── requirements.txt            # Python dependencies
│   │
│   ├── backend/
│   │   └── app.py                  # Flask REST API with endpoints
│   │
│   └── frontend/
│       ├── src/
│       │   ├── App.jsx             # Main React component
│       │   ├── App.css             # Styling
│       │   └── main.jsx            # React entry point
│       ├── index.html
│       ├── package.json
│       └── vite.config.js
│
├── Student_Performance_Predictor_Document.pdf
└── Student_Performance_Predictor_Document.docx
```

---

## 📊 Dataset Overview

The dataset contains **2000+ student records** with the following features:

| Feature | Type | Description |
|---|---|---|
| `StudentID` | Integer | Unique student identifier (1001+) |
| `Age` | Integer | Student age (15–18) |
| `Gender` | Categorical | MALE / FEMALE |
| `Ethnicity` | Categorical | Encoded ethnicity group |
| `Parental Education` | Integer | Education level (0–4) |
| `StudyTime Weekly` | Float | Weekly study hours |
| `Absences` | Integer | Number of absences |
| `Tutoring` | Binary | Tutoring support (0/1) |
| `Parental Support` | Integer | Support level (0–4) |
| `Cultural Activities` | Categorical | INTERESTED / NOT INTERESTED |
| `Sports` | Categorical | INTERESTED / NOT INTERESTED |
| `Music` | Categorical | INTERESTED / NOT INTERESTED |
| `Volunteering` | Binary | YES / NO |
| `GPA` | Float | **Target variable** (0.0 – 4.0) |
| `GradeClass` | Integer | Grade category (0–4) |

---

## 🤖 Machine Learning Model

### Algorithm: Custom Linear Regression with Gradient Descent

Built **from scratch** using only NumPy — no sklearn for the core model!

```python
# Key features used for prediction
selected_features = [
    'StudyTime Weekly',
    'Absences',
    'Parental Education',
    'Cultural Activities'
]
```

### Training Pipeline:

```
Raw CSV Data
    ↓
Data Cleaning (remove duplicates, handle nulls)
    ↓
Label Encoding (categorical → numerical)
    ↓
Custom StandardScaler (normalize features)
    ↓
Train/Test Split (80% train, 20% test)
    ↓
Gradient Descent (learning_rate=0.01, iterations=1000)
    ↓
Model Evaluation (MSE + R² Score)
    ↓
GPA Prediction
```

### Custom StandardScaler (built from scratch):
```python
class MyStandardScaler:
    def fit(self, X):
        self.mean_ = np.mean(X, axis=0)
        self.scale_ = np.std(X, axis=0)
    
    def transform(self, X):
        return (X - self.mean_) / self.scale_
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **ML Core** | Python, NumPy | Custom Gradient Descent model |
| **Data Processing** | Pandas, Scikit-learn | Data loading, encoding, evaluation |
| **Backend** | Flask, Flask-CORS | REST API server |
| **Production Server** | Waitress | WSGI production server |
| **Frontend** | React 18 + Vite | Interactive UI |
| **Styling** | CSS3 | Responsive card design |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/chakriburidi237-crypto/Student_performance_prediction.git
cd Student_performance_prediction/STUDENT\ GPA\ PREDICTOR
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
flask==3.0.0
flask-cors==4.0.0
pandas==2.1.4
numpy==1.26.3
scikit-learn==1.3.2
waitress==2.1.2
```

### Install Frontend Dependencies

```bash
cd frontend
npm install
```

---

## ▶️ Running the Application

### Option 1 — Full Stack (Recommended)

```bash
# Terminal 1: Start Backend (from STUDENT GPA PREDICTOR folder)
cd backend
python app.py
# Server starts at http://127.0.0.1:8080

# Terminal 2: Start Frontend
cd frontend
npm run dev
# Frontend starts at http://localhost:5173
```

### Option 2 — ML Script Only (Command Line)

```bash
# Run the ML model directly
python student_gpa_prediction.py

# Output:
# --- Student Details Search ---
# Enter Student ID to search: 1001
#
# Details for Student ID 1001:
#   StudentID: 1001
#   Age: 17
#   GPA: 2.93
#   GradeClass: 2
#   ...
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves frontend HTML |
| `GET` | `/api/student/<id>` | Get student data by ID |

### Example API Response:

```bash
GET /api/student/1001
```

```json
{
  "StudentID": 1001,
  "Age": 17,
  "Gender": 0,
  "Ethnicity": 0,
  "Parental Education": 2,
  "StudyTime Weekly": 19.83,
  "Absences": 7,
  "Tutoring": 1,
  "Parental Support": 2,
  "Cultural Activities": 0,
  "Sports": 0,
  "Music": 1,
  "Volunteering": 0,
  "GPA": 2.9292,
  "GradeClass": 2
}
```

---

## 🎨 Frontend — How It Works

```
User enters Student ID
        ↓
React fetches /api/student/{id}
        ↓
Flask queries the dataset
        ↓
Returns student JSON data
        ↓
StudentCard renders:
  • Student profile details
  • All academic attributes
  • Predicted GPA (4 decimal precision)
  • Grade Class badge
```

---

## 📈 Model Performance

| Metric | Value |
|---|---|
| **Algorithm** | Linear Regression (Gradient Descent) |
| **Learning Rate** | 0.01 |
| **Iterations** | 1000 |
| **Train/Test Split** | 80% / 20% |
| **Evaluation** | MSE + R² Score |

---

## 🔮 Future Improvements

- [ ] 🌲 Add Random Forest & XGBoost models for comparison
- [ ] 📊 Add data visualization dashboard (charts, graphs)
- [ ] 🔐 Add student login authentication
- [ ] 📱 Make frontend fully mobile responsive
- [ ] 🧠 Add real-time GPA prediction form (input features manually)
- [ ] 📤 Export student report as PDF
- [ ] 🐳 Dockerize the full application

---

## 👨‍💻 Developer

<div align="center">

**Surya Chakradhar Buridi**

*AI/ML Engineer | B.E. Artificial Intelligence & Machine Learning @ KIET*
*Ex-Industrial Trainee @ Schneider Electric, Bengaluru*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/surya-chakradhar-buridi-767548355)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/chakriburidi237-crypto)

</div>

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00f2fe,100:4facfe&height=100&section=footer" width="100%"/>

**⭐ If this project helped you, please give it a star!**

*Built with ❤️ by Surya Chakradhar Buridi*
*Associated with Kakinada Institute of Engineering and Technology (KIET)*

</div>
