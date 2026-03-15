"""
Flask Application for Student Performance Predictor
Works both locally and on PythonAnywhere
"""
import os
import sys
import numpy as np
import pandas as pd
from flask import Flask, jsonify, send_file
from flask_cors import CORS
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
CORS(app)

# Global variable for data
data = None

def load_data():
    """Load and preprocess the student data."""
    global data
    
    if data is not None:
        return data
    
    # Try different paths for the CSV file
    possible_paths = [
        os.path.join(BASE_DIR, 'Student_performance_data .csv'),
        'Student_performance_data .csv',
    ]
    
    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            break
    
    if file_path is None:
        print("ERROR: Could not find 'Student_performance_data .csv'")
        return None
    
    print(f"Loading data from: {file_path}")
    
    try:
        data = pd.read_csv(file_path)
        print(f"Loaded {len(data)} records successfully!")
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
    # Handle duplicates
    duplicates = data.duplicated().sum()
    if duplicates > 0:
        data.drop_duplicates(inplace=True)
    
    # Data Cleaning
    data.replace([np.inf, -np.inf], np.nan, inplace=True)
    data.fillna(data.mean(numeric_only=True), inplace=True)
    
    # Encoding Categorical Variables
    label_encoder = LabelEncoder()
    categorical_columns = data.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        data[col] = label_encoder.fit_transform(data[col])
    
    print("Data preprocessing complete!")
    return data

def get_student_data(student_id):
    """Get student data by ID."""
    global data
    
    if data is None:
        load_data()
    
    if data is None:
        return None
    
    try:
        student = data[data['StudentID'] == student_id]
        if not student.empty:
            return student.iloc[0].to_dict()
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Load data on startup
print("=" * 50)
print("  Student Performance Predictor")
print("=" * 50)
load_data()

# Routes
@app.route('/')
def index():
    index_path = os.path.join(BASE_DIR, 'index.html')
    return send_file(index_path)

@app.route('/api/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student_data = get_student_data(student_id)
    if student_data:
        clean_data = {}
        for k, v in student_data.items():
            try:
                if hasattr(v, 'item'):
                    clean_data[k] = v.item()
                else:
                    clean_data[k] = v
            except:
                clean_data[k] = str(v)
        return jsonify(clean_data)
    else:
        return jsonify({"error": "Student not found"}), 404

# Main entry point
if __name__ == '__main__':
    from waitress import serve
    print("")
    print("  ✅ Server running at: http://127.0.0.1:8080")
    print("  📊 Open in browser to use the app!")
    print("")
    print("=" * 50)
    serve(app, host='0.0.0.0', port=8080)
