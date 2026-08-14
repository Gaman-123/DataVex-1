# 🎙️ InterviewAI (DataVex-1)

Welcome to **InterviewAI**, your intelligent, automated technical interview platform! This project leverages advanced AI models to simulate a real-world technical interview experience.

## 🎯 Purpose

The purpose of InterviewAI is to provide an immersive, conversational interview environment. It helps companies streamline their hiring processes and provides candidates with a realistic, low-stress space to practice and showcase their skills. By utilizing a multi-agent architecture, the system mimics human interviewers by dynamically asking questions, probing deeper into responses, and providing comprehensive evaluations.

## 🔄 How the Interview Works

The interview is designed to feel just like a natural conversation with a real hiring manager or technical lead:

1. **The Interviewer Speaks First**: The session begins with the AI interviewer introducing itself and presenting the first question based on the candidate's resume or the job requirements.
2. **The Candidate Responds**: The candidate provides their answer in real-time. 
3. **Dynamic Depth Probing**: Instead of simply moving to the next question, the AI listens to the response. If the candidate mentions an interesting concept or leaves a gap, the **Depth Prober Agent** jumps in to ask follow-up questions, just like a real interviewer would.
4. **Voice & Confidence Analysis**: Throughout the session, the **Voice Confidence Agent** analyzes the delivery, pacing, and certainty of the candidate's responses.
5. **Real-time Evaluation**: Once the topic is sufficiently covered, the **Evaluator Agent** silently grades the responses in the background, updating the candidate's profile with actionable analytics.
6. **Moving Forward**: The **Orchestrator Agent** seamlessly transitions the conversation to the next topic or concludes the interview.

## 🚀 Features

- **Multi-Agent Architecture**: Dedicated AI agents for orchestrating, questioning, probing, and evaluating.
- **Real-Time Websocket Communication**: Ensures low latency and a smooth conversational flow between the frontend and backend.
- **Analytics Dashboard**: Comprehensive scoring and feedback available for both candidates and companies.
- **Resume Integration**: The AI tailors its questions directly to the experiences and skills listed on the candidate's resume.

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, WebSockets
- **AI/LLM**: Integration with Groq for lightning-fast inference
- **Frontend**: Designed to seamlessly connect with our robust backend APIs

## 🏃‍♂️ Getting Started

### Prerequisites
- Python 3.9+
- Node.js (for the frontend, if applicable)
- Groq API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Gaman-123/DataVex-1.git
   cd DataVex-1
   ```

2. **Set up the backend environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Create a `.env` file in the backend directory and add your API keys:
   ```env
   GROQ_API_KEY=your_api_key_here
   FRONTEND_URL=http://localhost:3000
   ```

4. **Run the backend**
   ```bash
   uvicorn main:app --reload
   ```

The backend API will be available at `http://localhost:8000`.

---
*Built with ❤️ to revolutionize the technical interview process.*
