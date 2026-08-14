import React from 'react';

const Candidates = () => {
  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1 style={{ margin: 0, fontSize: '2rem', fontWeight: 'normal', color: 'var(--text-dark)' }}>Candidates</h1>
        <button className="btn btn-primary">+ Add Candidate</button>
      </div>

      <div className="card" style={{ marginBottom: '1.5rem', display: 'flex', gap: '1rem', padding: '1rem' }}>
        <input 
          type="text" 
          placeholder="Search candidates by name or email..." 
          style={{ flex: 1, padding: '0.5rem', border: '1px solid var(--border-color)', borderRadius: '4px', fontSize: '1rem' }}
        />
        <select style={{ padding: '0.5rem', border: '1px solid var(--border-color)', borderRadius: '4px', fontSize: '1rem', minWidth: '150px' }}>
          <option>All Roles</option>
          <option>Frontend Engineer</option>
          <option>Backend Developer</option>
          <option>Data Scientist</option>
        </select>
        <button className="btn" style={{ backgroundColor: 'var(--background-light)', border: '1px solid var(--border-color)' }}>Filter</button>
      </div>

      <div className="card">
        <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
          <thead>
            <tr style={{ borderBottom: '2px solid var(--border-color)' }}>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Name</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Email</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Applied Role</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Interviews</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Avg. Score</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr style={{ borderBottom: '1px solid var(--border-color)' }}>
              <td style={{ padding: '1rem 0.5rem', fontWeight: '500' }}>Jane Doe</td>
              <td style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)' }}>jane.doe@example.com</td>
              <td style={{ padding: '1rem 0.5rem' }}>Frontend Engineer</td>
              <td style={{ padding: '1rem 0.5rem' }}>2</td>
              <td style={{ padding: '1rem 0.5rem' }}>84%</td>
              <td style={{ padding: '1rem 0.5rem' }}><a href="#" style={{ fontSize: '0.9rem' }}>View Profile</a></td>
            </tr>
            <tr style={{ borderBottom: '1px solid var(--border-color)' }}>
              <td style={{ padding: '1rem 0.5rem', fontWeight: '500' }}>John Smith</td>
              <td style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)' }}>john.smith@example.com</td>
              <td style={{ padding: '1rem 0.5rem' }}>Backend Developer</td>
              <td style={{ padding: '1rem 0.5rem' }}>1</td>
              <td style={{ padding: '1rem 0.5rem' }}>--</td>
              <td style={{ padding: '1rem 0.5rem' }}><a href="#" style={{ fontSize: '0.9rem' }}>View Profile</a></td>
            </tr>
             <tr style={{ borderBottom: '1px solid var(--border-color)' }}>
              <td style={{ padding: '1rem 0.5rem', fontWeight: '500' }}>Emily Davis</td>
              <td style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)' }}>emily.d@example.com</td>
              <td style={{ padding: '1rem 0.5rem' }}>Product Manager</td>
              <td style={{ padding: '1rem 0.5rem' }}>3</td>
              <td style={{ padding: '1rem 0.5rem' }}>92%</td>
              <td style={{ padding: '1rem 0.5rem' }}><a href="#" style={{ fontSize: '0.9rem' }}>View Profile</a></td>
            </tr>
            <tr>
              <td style={{ padding: '1rem 0.5rem', fontWeight: '500' }}>Michael Brown</td>
              <td style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)' }}>mbrown88@example.com</td>
              <td style={{ padding: '1rem 0.5rem' }}>DevOps Engineer</td>
              <td style={{ padding: '1rem 0.5rem' }}>1</td>
              <td style={{ padding: '1rem 0.5rem' }}>68%</td>
              <td style={{ padding: '1rem 0.5rem' }}><a href="#" style={{ fontSize: '0.9rem' }}>View Profile</a></td>
            </tr>
          </tbody>
        </table>
        
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '1.5rem', padding: '0.5rem' }}>
          <span style={{ color: 'var(--secondary-color)', fontSize: '0.9rem' }}>Showing 1 to 4 of 28 candidates</span>
          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <button className="btn" style={{ backgroundColor: 'var(--background-light)', border: '1px solid var(--border-color)', padding: '0.25rem 0.75rem' }}>Previous</button>
            <button className="btn btn-primary" style={{ padding: '0.25rem 0.75rem' }}>1</button>
            <button className="btn" style={{ backgroundColor: 'var(--background-light)', border: '1px solid var(--border-color)', padding: '0.25rem 0.75rem' }}>2</button>
            <button className="btn" style={{ backgroundColor: 'var(--background-light)', border: '1px solid var(--border-color)', padding: '0.25rem 0.75rem' }}>3</button>
            <button className="btn" style={{ backgroundColor: 'var(--background-light)', border: '1px solid var(--border-color)', padding: '0.25rem 0.75rem' }}>Next</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Candidates;
