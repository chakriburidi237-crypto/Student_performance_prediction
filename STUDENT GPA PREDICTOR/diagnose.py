import pandas as pd
import numpy as np
try:
    df = pd.read_csv("Student_performance_data .csv")
    print("Data loaded.")
    print("Dtypes:")
    print(df[['StudyTime Weekly', 'Absences', 'Parental Education', 'Cultural Activities', 'GPA']].dtypes)
    
    # Check for non-numeric
    non_numeric = df[['StudyTime Weekly', 'Absences', 'Parental Education', 'Cultural Activities']].select_dtypes(exclude=[np.number]).columns
    if len(non_numeric) > 0:
        print(f"Non-numeric columns found: {non_numeric.tolist()}")
    else:
        print("All feature columns are numeric.")

    # Check for zero std dev
    stds = df[['StudyTime Weekly', 'Absences', 'Parental Education', 'Cultural Activities']].std()
    print("Standard Deviations:")
    print(stds)
    if (stds == 0).any():
        print("WARNING: Zero variance column found!")

    # Test Scaler logic
    X = df[['StudyTime Weekly', 'Absences', 'Parental Education', 'Cultural Activities']].values
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    print(f"Calculated Means: {mean}")
    print(f"Calculated Stds: {std}")
    
    if (std == 0).any():
        print("CRITICAL: One of the columns has zero standard deviation, scaler will divide by zero.")

except Exception as e:
    print(f"Error: {e}")
    