import pytest
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

def test_dataset_exists_and_valid():
    csv_path = BASE_DIR / "student_performance_data.csv"
    assert csv_path.exists(), "Dataset student_performance_data.csv must exist in repository root"
    
    df = pd.read_csv(csv_path)
    assert len(df) > 0
    assert "StudentID" in df.columns or "GPA" in df.columns

def test_model_module_importable():
    import student_gpa_prediction as sgp
    data = sgp.load_data()
    assert data is not None
    assert len(data) > 0
