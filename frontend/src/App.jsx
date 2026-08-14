import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainLayout from './components/MainLayout';
import Dashboard from './pages/Dashboard';
import Candidates from './pages/Candidates';
import Sessions from './pages/Sessions';
import './App.css';

function App() {
  return (
    <Router>
      <MainLayout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/candidates" element={<Candidates />} />
          <Route path="/sessions" element={<Sessions />} />
        </Routes>
      </MainLayout>
    </Router>
  );
}

export default App;
