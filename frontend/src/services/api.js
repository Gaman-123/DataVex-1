const API_BASE_URL = 'http://localhost:8000';

export const fetchDashboardStats = async () => {
  // Mock fetch call for now, can be hooked to actual backend API
  // const response = await fetch(`${API_BASE_URL}/api/stats`);
  // return response.json();
  
  return {
    totalInterviews: 142,
    avgScore: 76,
    activeCandidates: 28
  };
};

export const fetchCandidates = async () => {
  // const response = await fetch(`${API_BASE_URL}/api/candidates`);
  // return response.json();
  return [];
};

export const createSession = async (sessionData) => {
  /*
  const response = await fetch(`${API_BASE_URL}/api/sessions`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(sessionData)
  });
  return response.json();
  */
  console.log("Creating session:", sessionData);
  return { success: true };
};
