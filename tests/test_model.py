import pytest
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

def test_dataset_exists_and_valid():
    csv_candidates = [
        BASE_DIR / "student_performance_data.csv",
        BASE_DIR / "Student_performance_data .csv"
    ]
    found = any(p.exists() for p in csv_candidates)
    assert found, "Dataset must exist in repository root"
    
    target = next(p for p in csv_candidates if p.exists())
    df = pd.read_csv(target)
    assert len(df) > 0
    assert "StudentID" in df.columns or "GPA" in df.columns

def test_model_module_importable():
    import student_gpa_prediction as sgp
    data = sgp.load_data()
    assert data is not None
    assert len(data) > 0
