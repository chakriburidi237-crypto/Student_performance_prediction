"""
Student Performance Prediction & Lookup Tool

Features:
- **Clean Interface**: Launches directly into a student search prompt.
- **Student ID Lookup**: Search for details by entering a Student ID (e.g., 1001).
- **Background Training**: The model trains silently upon startup.

Usage:
1. Run the script: `python student_gpa_prediction.py`
2. Wait for the model training to complete (short pause).
3. Enter a valid Student ID when prompted.
4. Type 'exit' to quit.
"""
import numpy as np
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

# Global variable to store loaded data
data = None

def get_data_path():
    """Get the correct path to the CSV file."""
    # Try current directory first
    if os.path.exists("Student_performance_data .csv"):
        return "Student_performance_data .csv"
    # Try parent directory (when running from backend folder)
    parent_path = os.path.join(os.path.dirname(__file__), "..", "Student_performance_data .csv")
    if os.path.exists(parent_path):
        return parent_path
    # Try same directory as this script
    script_path = os.path.join(os.path.dirname(__file__), "Student_performance_data .csv")
    if os.path.exists(script_path):
        return script_path
    return "Student_performance_data .csv"

def load_data():
    """Load and preprocess the student data."""
    global data
    
    if data is not None:
        return data
    
    file_path = get_data_path()
    
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        print(f"An error occurred while loading the dataset: {e}")
        return None
    
    # Handle duplicates
    duplicates = data.duplicated().sum()
    if duplicates > 0:
        data.drop_duplicates(inplace=True)
    
    # Data Cleaning
    data.replace([np.inf, -np.inf], np.nan, inplace=True)
    data.fillna(data.mean(numeric_only=True), inplace=True)
    
    # Encoding Categorical Variables
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    categorical_columns = data.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        data[col] = label_encoder.fit_transform(data[col])
    
    return data

def get_student_data(student_id):
    """
    Search for a student by ID and return their details as a dictionary.
    Returns None if not found.
    """
    global data
    
    # Ensure data is loaded
    if data is None:
        load_data()
    
    if data is None:
        return None
    
    try:
        student = data[data['StudentID'] == student_id]
        if not student.empty:
            return student.iloc[0].to_dict()
        else:
            return None
    except Exception as e:
        print(f"An error occurred during search: {e}")
        return None

def get_student_details(student_id):
    """
    Search for a student by ID and print their details.
    """
    student_dict = get_student_data(student_id)
    if student_dict:
        print(f"\nDetails for Student ID {student_id}:")
        for key, value in student_dict.items():
            print(f"  {key}: {value}")
    else:
        print(f"\nStudent ID {student_id} not found.")

# ============================================
# Training and visualization code below
# Only runs when script is executed directly
# ============================================

def run_training():
    """Run the model training pipeline."""
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score
    
    global data
    
    # Ensure data is loaded
    if data is None:
        load_data()
    
    if data is None:
        print("Failed to load data. Exiting.")
        return
    
    # Custom StandardScaler class
    class MyStandardScaler:
        def __init__(self):
            self.mean_ = None
            self.scale_ = None
        
        def fit(self, X):
            X = np.asarray(X)
            self.mean_ = np.mean(X, axis=0)
            self.scale_ = np.std(X, axis=0)
        
        def transform(self, X):
            if self.mean_ is None or self.scale_ is None:
                raise ValueError("The scaler has not been fitted yet.")
            return (X - self.mean_) / self.scale_
        
        def fit_transform(self, X):
            self.fit(X)
            return self.transform(X)
    
    # Data Preparation
    selected_features = ['StudyTime Weekly', 'Absences', 'Parental Education', 'Cultural Activities']
    X_raw = data[selected_features]
    Y = data['GPA'].values
    
    X_train_raw, X_test_raw, Y_train, Y_test = train_test_split(
        X_raw, Y, test_size=0.2, random_state=42
    )
    
    # Scale the data
    scaler = MyStandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_raw)
    X_test_scaled = scaler.transform(X_test_raw)
    
    # Gradient Descent Functions
    def predict(X, w, b):
        return np.dot(X, w) + b
    
    def cost_function(X, y, w, b):
        m = len(y)
        predictions = predict(X, w, b)
        cost = (1.0 / (2 * m)) * np.sum((predictions - y) ** 2)
        return cost
    
    def gradient_descent(X, y, learning_rate, iterations):
        m, n = X.shape
        w = np.zeros(n)
        b = 0.0
        cost_history = []
        
        for i in range(iterations):
            predictions = predict(X, w, b)
            errors = predictions - y
            
            dw = (1.0 / m) * np.dot(X.T, errors)
            db = (1.0 / m) * np.sum(errors)
            
            w = w - learning_rate * dw
            b = b - learning_rate * db
            
            cost = cost_function(X, y, w, b)
            cost_history.append(cost)
        
        return w, b, cost_history
    
    # Train the model
    learning_rate = 0.01
    iterations = 1000
    w_learned, b_learned, cost_history = gradient_descent(X_train_scaled, Y_train, learning_rate, iterations)
    
    # Evaluate
    y_train_pred = predict(X_train_scaled, w_learned, b_learned)
    y_test_pred = predict(X_test_scaled, w_learned, b_learned)
    
    train_mse = mean_squared_error(Y_train, y_train_pred)
    test_mse = mean_squared_error(Y_test, y_test_pred)
    train_r2 = r2_score(Y_train, y_train_pred)
    test_r2 = r2_score(Y_test, y_test_pred)
    
    # Training is complete (silently)
    return w_learned, b_learned

def run_interactive_search():
    """Run the interactive student search loop."""
    print("\n--- Student Details Search ---")
    print("Enter 'exit' to quit.")
    
    while True:
        try:
            user_input = input("\nEnter Student ID to search: ")
            
            if user_input.strip().lower() == 'exit':
                print("Exiting search.")
                break
            
            student_id = int(user_input)
            get_student_details(student_id)
        except ValueError:
            print("Invalid input. Please enter a numeric Student ID.")
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nSearch interrupted by user. Exiting.")
            break

# Main entry point
if __name__ == "__main__":
    # Load data and train model when run directly
    load_data()
    run_training()
    run_interactive_search()
