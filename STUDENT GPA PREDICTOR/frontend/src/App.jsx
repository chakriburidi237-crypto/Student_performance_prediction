import React, { useState } from 'react';
import './App.css';

function App() {
    const [studentId, setStudentId] = useState('');
    const [studentData, setStudentData] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSearch = async (e) => {
        e.preventDefault();
        if (!studentId) return;

        setLoading(true);
        setError(null);
        setStudentData(null);

        try {
            // In development, Vite proxys /api to Flask
            // If running separately without proxy, use http://127.0.0.1:5000/api/student/${studentId}
            const response = await fetch(`/api/student/${studentId}`);

            if (!response.ok) {
                throw new Error('Student not found');
            }

            const data = await response.json();
            setStudentData(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="container">
            <header>
                <h1>Student Insights</h1>
                <p className="subtitle">Performance Prediction & Analytics System</p>
            </header>

            <form className="search-section" onSubmit={handleSearch}>
                <input
                    type="number"
                    placeholder="Enter Student ID (e.g. 1001)"
                    value={studentId}
                    onChange={(e) => setStudentId(e.target.value)}
                />
                <button type="submit" disabled={loading}>
                    {loading ? 'Searching...' : 'Search'}
                </button>
            </form>

            {error && (
                <div className="error-message">
                    <p>⚠️ {error}</p>
                </div>
            )}

            {studentData && (
                <div className="result-section">
                    <StudentCard student={studentData} />
                </div>
            )}
        </div>
    );
}

function StudentCard({ student }) {
    // Helper to format values
    const formatValue = (key, val) => {
        if (typeof val === 'number' && !Number.isInteger(val)) {
            return val.toFixed(2);
        }
        return val;
    };

    // Separate main details from list
    const { StudentID, GPA, GradeClass, ...otherDetails } = student;

    return (
        <div className="student-card">
            <div className="card-header">
                <div>
                    <div className="label">Student Profile</div>
                    <h2>ID: {StudentID}</h2>
                </div>
                <div className="badge">Class {GradeClass}</div>
            </div>

            <div className="grid">
                {Object.entries(otherDetails).map(([key, value]) => (
                    <div className="info-item" key={key}>
                        <span className="label">{key.replace(/([A-Z])/g, ' $1').trim()}</span>
                        <span className="value">{formatValue(key, value)}</span>
                    </div>
                ))}
            </div>

            <div className="gpa-card">
                <div className="info-item">
                    <span className="label">Predicted GPA</span>
                    <span className="value">{typeof GPA === 'number' ? GPA.toFixed(4) : GPA}</span>
                </div>
            </div>
        </div>
    );
}

export default App;
