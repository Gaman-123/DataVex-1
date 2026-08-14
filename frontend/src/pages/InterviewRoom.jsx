import React, { useState } from 'react';

const InterviewRoom = () => {
  const [isRecording, setIsRecording] = useState(false);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%', minHeight: '80vh' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
        <div>
          <h2 style={{ margin: 0, fontWeight: '500' }}>Active Session: John Smith</h2>
          <span style={{ color: 'var(--secondary-color)', fontSize: '0.9rem' }}>System Design - Software Engineer Level III</span>
        </div>
        <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
          <span style={{ fontSize: '1.2rem', fontWeight: 'bold', color: 'var(--secondary-color)', fontFamily: 'monospace' }}>00:14:23</span>
          <button className="btn" style={{ backgroundColor: '#dc3545', color: '#fff', border: 'none' }}>End Session</button>
        </div>
      </div>

      <div style={{ display: 'flex', gap: '1.5rem', flex: 1 }}>
        {/* Left Pane: Transcript and Logs */}
        <div className="card" style={{ flex: 2, display: 'flex', flexDirection: 'column', marginBottom: 0 }}>
          <h3 style={{ marginTop: 0, borderBottom: '1px solid var(--border-color)', paddingBottom: '0.5rem', fontWeight: '500' }}>Live Transcript</h3>
          <div style={{ flex: 1, overflowY: 'auto', padding: '1rem 0', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start' }}>
              <span style={{ fontSize: '0.8rem', color: 'var(--secondary-color)', marginBottom: '0.25rem' }}>AI Interviewer • 10:01 AM</span>
              <div style={{ backgroundColor: '#f1f3f4', padding: '0.75rem 1rem', borderRadius: '0.5rem', borderBottomLeftRadius: '0' }}>
                Welcome John. To start off, could you walk me through a complex system you designed recently and explain the trade-offs you had to make?
              </div>
            </div>
            
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end' }}>
              <span style={{ fontSize: '0.8rem', color: 'var(--secondary-color)', marginBottom: '0.25rem' }}>John Smith • 10:02 AM</span>
              <div style={{ backgroundColor: '#e8f0fe', color: '#1967d2', padding: '0.75rem 1rem', borderRadius: '0.5rem', borderBottomRightRadius: '0', maxWidth: '80%' }}>
                Sure. Recently I designed a distributed caching layer for our microservices...
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start' }}>
              <span style={{ fontSize: '0.8rem', color: '#b06000', marginBottom: '0.25rem' }}>Depth Prober Agent • 10:05 AM</span>
              <div style={{ backgroundColor: '#fef7e0', padding: '0.75rem 1rem', borderRadius: '0.5rem', borderBottomLeftRadius: '0' }}>
                That's interesting. You mentioned using Redis for the cache. How did you handle cache invalidation in a multi-region deployment?
              </div>
            </div>
          </div>
          <div style={{ borderTop: '1px solid var(--border-color)', paddingTop: '1rem', display: 'flex', alignItems: 'center', gap: '1rem' }}>
             <div style={{ flex: 1, padding: '0.75rem', border: '1px solid var(--border-color)', borderRadius: '4px', color: 'var(--secondary-color)', fontStyle: 'italic' }}>
               Microphone is active...
             </div>
             <button 
               className="btn" 
               style={{ backgroundColor: isRecording ? '#dc3545' : 'var(--primary-color)', color: '#fff' }}
               onClick={() => setIsRecording(!isRecording)}
             >
               {isRecording ? 'Mute' : 'Unmute'}
             </button>
          </div>
        </div>

        {/* Right Pane: Controls and AI Status */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <div className="card" style={{ marginBottom: 0 }}>
             <h3 style={{ marginTop: 0, fontWeight: '500', borderBottom: '1px solid var(--border-color)', paddingBottom: '0.5rem' }}>Current Evaluation</h3>
             <div style={{ paddingTop: '1rem' }}>
               <div style={{ marginBottom: '1rem' }}>
                 <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.25rem' }}>
                   <span style={{ fontSize: '0.9rem', fontWeight: '500' }}>System Architecture</span>
                   <span style={{ fontSize: '0.9rem', fontWeight: 'bold', color: '#1e8e3e' }}>Strong</span>
                 </div>
                 <div style={{ height: '8px', width: '100%', backgroundColor: '#e9ecef', borderRadius: '4px' }}>
                   <div style={{ height: '100%', width: '85%', backgroundColor: '#1e8e3e', borderRadius: '4px' }}></div>
                 </div>
               </div>
               
               <div style={{ marginBottom: '1rem' }}>
                 <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.25rem' }}>
                   <span style={{ fontSize: '0.9rem', fontWeight: '500' }}>Communication</span>
                   <span style={{ fontSize: '0.9rem', fontWeight: 'bold', color: 'var(--primary-color)' }}>Good</span>
                 </div>
                 <div style={{ height: '8px', width: '100%', backgroundColor: '#e9ecef', borderRadius: '4px' }}>
                   <div style={{ height: '100%', width: '70%', backgroundColor: 'var(--primary-color)', borderRadius: '4px' }}></div>
                 </div>
               </div>
             </div>
          </div>

          <div className="card" style={{ marginBottom: 0, flex: 1 }}>
             <h3 style={{ marginTop: 0, fontWeight: '500', borderBottom: '1px solid var(--border-color)', paddingBottom: '0.5rem' }}>System Controls</h3>
             <div style={{ paddingTop: '1rem', display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
               <button className="btn" style={{ border: '1px solid var(--border-color)', width: '100%', textAlign: 'left' }}>Next Topic</button>
               <button className="btn" style={{ border: '1px solid var(--border-color)', width: '100%', textAlign: 'left' }}>Request Clarification</button>
               <button className="btn" style={{ border: '1px solid var(--border-color)', width: '100%', textAlign: 'left' }}>Override Score</button>
             </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InterviewRoom;
