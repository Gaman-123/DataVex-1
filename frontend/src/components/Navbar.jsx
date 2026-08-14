import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <header style={{ backgroundColor: '#ffffff', borderBottom: '1px solid var(--border-color)', padding: '1rem 2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
        <h2 style={{ margin: 0, color: 'var(--primary-color)', fontSize: '1.5rem', fontWeight: '600' }}>InterviewAI</h2>
      </div>
      <nav style={{ display: 'flex', gap: '1.5rem' }}>
        <Link to="/" style={{ color: 'var(--text-dark)', fontWeight: '500' }}>Dashboard</Link>
        <Link to="/candidates" style={{ color: 'var(--text-dark)', fontWeight: '500' }}>Candidates</Link>
        <Link to="/sessions" style={{ color: 'var(--text-dark)', fontWeight: '500' }}>Sessions</Link>
      </nav>
      <div>
        <div style={{ width: '35px', height: '35px', borderRadius: '50%', backgroundColor: 'var(--primary-color)', color: 'white', display: 'flex', justifyContent: 'center', alignItems: 'center', fontWeight: 'bold' }}>
          AD
        </div>
      </div>
    </header>
  );
};

export default Navbar;
