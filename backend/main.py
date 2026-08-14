from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import companies, candidates, sessions, analytics
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="InterviewAI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(companies.router)
app.include_router(candidates.router)
app.include_router(sessions.router)
app.include_router(analytics.router)

@app.get("/")
async def root():
    return {"status": "InterviewAI running"}

@app.get("/health")
async def health():
    return {"status": "ok"}
