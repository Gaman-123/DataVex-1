import React from 'react';
import Navbar from './Navbar';

const MainLayout = ({ children }) => {
  return (
    <div className="app-container" style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh', backgroundColor: 'var(--background-light)' }}>
      <Navbar />
      <main className="main-content" style={{ flex: 1, padding: '2rem' }}>
        <div className="container" style={{ maxWidth: '1200px', margin: '0 auto', width: '100%' }}>
          {children}
        </div>
      </main>
      <footer style={{ backgroundColor: '#ffffff', borderTop: '1px solid var(--border-color)', padding: '1.5rem 0', textAlign: 'center', color: 'var(--secondary-color)', fontSize: '0.9rem' }}>
        <div className="container">
          <p style={{ margin: 0 }}>&copy; 2024 InterviewAI Platform. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default MainLayout;
