import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app-container">
        {/* Placeholder Navbar */}
        <header style={{ backgroundColor: '#fff', borderBottom: '1px solid #dee2e6', padding: '1rem 0' }}>
          <div className="container" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h4 style={{ margin: 0, color: '#0056b3' }}>InterviewAI</h4>
            <nav>
              <Link to="/" style={{ marginRight: '1rem', color: '#333' }}>Dashboard</Link>
            </nav>
          </div>
        </header>

        <main className="main-content">
          <Routes>
            <Route path="/" element={<div className="container"><h1>Dashboard</h1><p>Welcome to the admin panel.</p></div>} />
          </Routes>
        </main>

        <footer style={{ backgroundColor: '#343a40', color: '#fff', padding: '2rem 0', textAlign: 'center' }}>
          <div className="container">
            <p style={{ margin: 0 }}>&copy; 2024 InterviewAI Platform. All rights reserved.</p>
          </div>
        </footer>
      </div>
    </Router>
  );
}

export default App;
