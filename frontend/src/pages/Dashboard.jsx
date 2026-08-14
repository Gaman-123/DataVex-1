import React from 'react';

const Dashboard = () => {
  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1 style={{ margin: 0, fontSize: '2rem', fontWeight: 'normal', color: 'var(--text-dark)' }}>Dashboard</h1>
        <button className="btn btn-primary">+ New Interview Session</button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1.5rem', marginBottom: '2rem' }}>
        <div className="card" style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
          <span style={{ color: 'var(--secondary-color)', fontSize: '0.9rem', textTransform: 'uppercase', letterSpacing: '1px' }}>Total Interviews</span>
          <span style={{ fontSize: '2.5rem', fontWeight: 'bold' }}>142</span>
        </div>
        <div className="card" style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
          <span style={{ color: 'var(--secondary-color)', fontSize: '0.9rem', textTransform: 'uppercase', letterSpacing: '1px' }}>Avg. Score</span>
          <span style={{ fontSize: '2.5rem', fontWeight: 'bold' }}>76%</span>
        </div>
        <div className="card" style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
          <span style={{ color: 'var(--secondary-color)', fontSize: '0.9rem', textTransform: 'uppercase', letterSpacing: '1px' }}>Active Candidates</span>
          <span style={{ fontSize: '2.5rem', fontWeight: 'bold' }}>28</span>
        </div>
      </div>

      <div className="card">
        <h3 style={{ marginTop: 0, marginBottom: '1.5rem', fontWeight: '500' }}>Recent Activity</h3>
        <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
          <thead>
            <tr style={{ borderBottom: '2px solid var(--border-color)' }}>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Candidate</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Role</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Date</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Status</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr style={{ borderBottom: '1px solid var(--border-color)' }}>
              <td style={{ padding: '1rem 0.5rem' }}>Jane Doe</td>
              <td style={{ padding: '1rem 0.5rem' }}>Frontend Engineer</td>
              <td style={{ padding: '1rem 0.5rem' }}>Oct 24, 2024</td>
              <td style={{ padding: '1rem 0.5rem' }}><span style={{ padding: '0.25rem 0.5rem', backgroundColor: '#e6f4ea', color: '#1e8e3e', borderRadius: '4px', fontSize: '0.85rem' }}>Completed</span></td>
              <td style={{ padding: '1rem 0.5rem' }}><a href="#" style={{ fontSize: '0.9rem' }}>View Results</a></td>
            </tr>
            <tr style={{ borderBottom: '1px solid var(--border-color)' }}>
              <td style={{ padding: '1rem 0.5rem' }}>John Smith</td>
              <td style={{ padding: '1rem 0.5rem' }}>Backend Developer</td>
              <td style={{ padding: '1rem 0.5rem' }}>Oct 24, 2024</td>
              <td style={{ padding: '1rem 0.5rem' }}><span style={{ padding: '0.25rem 0.5rem', backgroundColor: '#fef7e0', color: '#b06000', borderRadius: '4px', fontSize: '0.85rem' }}>In Progress</span></td>
              <td style={{ padding: '1rem 0.5rem' }}><a href="#" style={{ fontSize: '0.9rem' }}>Join Session</a></td>
            </tr>
            <tr>
              <td style={{ padding: '1rem 0.5rem' }}>Alice Johnson</td>
              <td style={{ padding: '1rem 0.5rem' }}>Data Scientist</td>
              <td style={{ padding: '1rem 0.5rem' }}>Oct 23, 2024</td>
              <td style={{ padding: '1rem 0.5rem' }}><span style={{ padding: '0.25rem 0.5rem', backgroundColor: '#e6f4ea', color: '#1e8e3e', borderRadius: '4px', fontSize: '0.85rem' }}>Completed</span></td>
              <td style={{ padding: '1rem 0.5rem' }}><a href="#" style={{ fontSize: '0.9rem' }}>View Results</a></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Dashboard;
