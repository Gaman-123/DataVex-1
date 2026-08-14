from groq import AsyncGroq
from dotenv import load_dotenv
import os

load_dotenv()

client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

MODELS = {
    "fast":  "llama3-8b-8192",
    "smart": "llama3-70b-8192",
}

async def chat(
    messages: list[dict],
    model: str = "smart",
    temperature: float = 0.3,
    max_tokens: int = 2048,
    json_mode: bool = False,
) -> str:
    kwargs = dict(
        model=MODELS[model],
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}

    response = await client.chat.completions.create(**kwargs)
    return response.choices[0].message.content