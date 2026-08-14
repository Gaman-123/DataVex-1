import React, { useState } from 'react';

const Sessions = () => {
  const [showForm, setShowForm] = useState(false);

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1 style={{ margin: 0, fontSize: '2rem', fontWeight: 'normal', color: 'var(--text-dark)' }}>Sessions</h1>
        <button className="btn btn-primary" onClick={() => setShowForm(!showForm)}>
          {showForm ? 'Cancel' : '+ Create Session'}
        </button>
      </div>

      {showForm && (
        <div className="card" style={{ marginBottom: '2rem' }}>
          <h3 style={{ marginTop: 0, marginBottom: '1.5rem', fontWeight: '500' }}>Create New Interview Session</h3>
          <form style={{ display: 'flex', flexDirection: 'column', gap: '1rem', maxWidth: '600px' }}>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              <label style={{ fontWeight: '500', color: 'var(--text-dark)' }}>Candidate</label>
              <select style={{ padding: '0.5rem', border: '1px solid var(--border-color)', borderRadius: '4px', fontSize: '1rem' }}>
                <option>Select a candidate...</option>
                <option>Jane Doe</option>
                <option>John Smith</option>
                <option>Emily Davis</option>
              </select>
            </div>
            
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              <label style={{ fontWeight: '500', color: 'var(--text-dark)' }}>Interview Type</label>
              <select style={{ padding: '0.5rem', border: '1px solid var(--border-color)', borderRadius: '4px', fontSize: '1rem' }}>
                <option>Technical Screen</option>
                <option>System Design</option>
                <option>Behavioral</option>
              </select>
            </div>

            <div style={{ display: 'flex', gap: '1rem' }}>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem', flex: 1 }}>
                <label style={{ fontWeight: '500', color: 'var(--text-dark)' }}>Date</label>
                <input type="date" style={{ padding: '0.5rem', border: '1px solid var(--border-color)', borderRadius: '4px', fontSize: '1rem' }} />
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem', flex: 1 }}>
                <label style={{ fontWeight: '500', color: 'var(--text-dark)' }}>Time</label>
                <input type="time" style={{ padding: '0.5rem', border: '1px solid var(--border-color)', borderRadius: '4px', fontSize: '1rem' }} />
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              <label style={{ fontWeight: '500', color: 'var(--text-dark)' }}>Notes / Focus Areas</label>
              <textarea rows="4" placeholder="Optional notes for the evaluator..." style={{ padding: '0.5rem', border: '1px solid var(--border-color)', borderRadius: '4px', fontSize: '1rem', fontFamily: 'inherit' }}></textarea>
            </div>

            <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
              <button type="button" className="btn btn-primary">Schedule Session</button>
              <button type="button" className="btn" style={{ border: '1px solid var(--border-color)' }} onClick={() => setShowForm(false)}>Cancel</button>
            </div>
          </form>
        </div>
      )}

      <div className="card">
        <h3 style={{ marginTop: 0, marginBottom: '1.5rem', fontWeight: '500' }}>Upcoming Sessions</h3>
        <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
          <thead>
            <tr style={{ borderBottom: '2px solid var(--border-color)' }}>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Candidate</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Type</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Scheduled Time</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Status</th>
              <th style={{ padding: '1rem 0.5rem', color: 'var(--secondary-color)', fontWeight: '600' }}>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr style={{ borderBottom: '1px solid var(--border-color)' }}>
              <td style={{ padding: '1rem 0.5rem', fontWeight: '500' }}>John Smith</td>
              <td style={{ padding: '1rem 0.5rem' }}>System Design</td>
              <td style={{ padding: '1rem 0.5rem' }}>Tomorrow, 10:00 AM</td>
              <td style={{ padding: '1rem 0.5rem' }}><span style={{ padding: '0.25rem 0.5rem', backgroundColor: '#e8f0fe', color: '#1967d2', borderRadius: '4px', fontSize: '0.85rem' }}>Scheduled</span></td>
              <td style={{ padding: '1rem 0.5rem' }}><a href="/interview" style={{ fontSize: '0.9rem', fontWeight: 'bold' }}>Start Session</a></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Sessions;
