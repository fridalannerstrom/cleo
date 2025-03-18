import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")  # För framtida autentisering
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # API-nyckeln för OpenAI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Läs in databasen URL från Render (eller använd en annan miljövariabel om du har den lokalt)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # Render ger denna URL