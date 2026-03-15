from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import sys
import os

# Add parent directory to path to import student_gpa_prediction
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from student_gpa_prediction import get_student_data

app = Flask(__name__)
# Enable CORS to allow requests from React frontend
CORS(app)

# Serve the frontend at the root URL
@app.route('/')
def index():
    return send_file(os.path.join(parent_dir, 'index.html'))

@app.route('/api/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student_data = get_student_data(student_id)
    if student_data:
        # Convert numpy types to native Python types for JSON serialization
        # (e.g., int64 -> int, float64 -> float)
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

if __name__ == '__main__':
    from waitress import serve
    print("=" * 50)
    print("  Student Performance Predictor")
    print("  Open in browser: http://127.0.0.1:8080")
    print("=" * 50)
    print("Press CTRL+C to quit")
    serve(app, host='0.0.0.0', port=8080)
