import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")  # För framtida autentisering
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # API-nyckeln för OpenAI