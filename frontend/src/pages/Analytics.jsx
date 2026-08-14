import React from 'react';

const Analytics = () => {
  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1 style={{ margin: 0, fontSize: '2rem', fontWeight: 'normal', color: 'var(--text-dark)' }}>Platform Analytics</h1>
        <div style={{ display: 'flex', gap: '1rem' }}>
          <select style={{ padding: '0.5rem', border: '1px solid var(--border-color)', borderRadius: '4px', fontSize: '1rem' }}>
            <option>Last 30 Days</option>
            <option>Last Quarter</option>
            <option>Year to Date</option>
          </select>
          <button className="btn btn-primary">Export Report</button>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.5rem', marginBottom: '2rem' }}>
        <div className="card">
          <h3 style={{ marginTop: 0, fontWeight: '500', color: 'var(--secondary-color)' }}>Pass Rate</h3>
          <div style={{ fontSize: '3rem', fontWeight: 'bold', margin: '1rem 0' }}>42%</div>
          <span style={{ color: '#1e8e3e', fontWeight: '500' }}>↑ 5% from last month</span>
        </div>
        <div className="card">
          <h3 style={{ marginTop: 0, fontWeight: '500', color: 'var(--secondary-color)' }}>Average Time to Hire</h3>
          <div style={{ fontSize: '3rem', fontWeight: 'bold', margin: '1rem 0' }}>14 Days</div>
          <span style={{ color: '#1e8e3e', fontWeight: '500' }}>↓ 2 days from last month</span>
        </div>
        <div className="card">
          <h3 style={{ marginTop: 0, fontWeight: '500', color: 'var(--secondary-color)' }}>Interviews Conducted</h3>
          <div style={{ fontSize: '3rem', fontWeight: 'bold', margin: '1rem 0' }}>318</div>
          <span style={{ color: 'var(--secondary-color)' }}>Total across all roles</span>
        </div>
      </div>

      <div className="card">
        <h3 style={{ marginTop: 0, marginBottom: '1.5rem', fontWeight: '500' }}>Skill Gap Analysis</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
              <span style={{ fontWeight: '500' }}>System Design</span>
              <span style={{ color: 'var(--secondary-color)' }}>Avg Score: 68%</span>
            </div>
            <div style={{ height: '12px', width: '100%', backgroundColor: '#e9ecef', borderRadius: '6px' }}>
              <div style={{ height: '100%', width: '68%', backgroundColor: '#fbbc04', borderRadius: '6px' }}></div>
            </div>
          </div>

          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
              <span style={{ fontWeight: '500' }}>Data Structures & Algorithms</span>
              <span style={{ color: 'var(--secondary-color)' }}>Avg Score: 85%</span>
            </div>
            <div style={{ height: '12px', width: '100%', backgroundColor: '#e9ecef', borderRadius: '6px' }}>
              <div style={{ height: '100%', width: '85%', backgroundColor: '#1e8e3e', borderRadius: '6px' }}></div>
            </div>
          </div>

          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
              <span style={{ fontWeight: '500' }}>Communication</span>
              <span style={{ color: 'var(--secondary-color)' }}>Avg Score: 92%</span>
            </div>
            <div style={{ height: '12px', width: '100%', backgroundColor: '#e9ecef', borderRadius: '6px' }}>
              <div style={{ height: '100%', width: '92%', backgroundColor: '#1e8e3e', borderRadius: '6px' }}></div>
            </div>
          </div>
          
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
              <span style={{ fontWeight: '500' }}>Cloud Architecture (AWS/GCP)</span>
              <span style={{ color: 'var(--secondary-color)' }}>Avg Score: 45%</span>
            </div>
            <div style={{ height: '12px', width: '100%', backgroundColor: '#e9ecef', borderRadius: '6px' }}>
              <div style={{ height: '100%', width: '45%', backgroundColor: '#ea4335', borderRadius: '6px' }}></div>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
};

export default Analytics;
