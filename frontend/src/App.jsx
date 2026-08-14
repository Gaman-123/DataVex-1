import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainLayout from './components/MainLayout';
import './App.css';

function App() {
  return (
    <Router>
      <MainLayout>
        <Routes>
          <Route path="/" element={
            <div className="card">
              <h1>Dashboard</h1>
              <p>Welcome to the admin panel.</p>
            </div>
          } />
        </Routes>
      </MainLayout>
    </Router>
  );
}

export default App;
